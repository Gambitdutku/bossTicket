from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password, check_password
from django.utils import timezone
from .models import User, UserEmail, UserAccount, Ticket, TicketCdata, TicketPriority, HelpTopic, Department, ThreadEntry, Staff, TicketStatus, Attachment
from django.core.files.storage import FileSystemStorage

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # use fake email id then update
        temp_user = User(org_id=0, status=1, name=name,
                         created=timezone.now(), updated=timezone.now(),
                         default_email_id=0)  # temp
        temp_user.save()

        # save email
        user_email = UserEmail(user_id=temp_user.id, flags=0, address=email)
        user_email.save()

        # update user table
        temp_user.default_email_id = user_email.id
        temp_user.save()

        # go girl you slay
        hashed_pw = make_password(password)
        account = UserAccount(user_id=temp_user.id, status=1,
                              username=email, passwd=hashed_pw,
                              registered=timezone.now())
        account.save()

        return redirect('login')
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user_email = UserEmail.objects.get(address=email)
            account = UserAccount.objects.get(user_id=user_email.user_id)
        except (UserEmail.DoesNotExist, UserAccount.DoesNotExist):
            # Error
            return render(request, 'login.html', {'error': 'Invalid credentials'})
        # Parolayı kontrol et
        if check_password(password, account.passwd):
            request.session['user_id'] = account.user_id  # save in session
            return redirect('ticket_list')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def create_ticket(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')

    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        help_topic_id = request.POST.get('help_topic')
        priority_id = request.POST.get('priority')
        dept_id = request.POST.get('department')

        # get email id
        try:
            user_email = UserEmail.objects.get(user_id=user_id)
        except UserEmail.DoesNotExist:
            return HttpResponse("User email not found.", status=400)

        ticket = Ticket(
            user_id=user_id,
            user_email_id=user_email.id,
            dept_id=dept_id,
            topic_id=help_topic_id,
            status_id=1,
            sla_id=1,  #
            staff_id=0,
            team_id=0,
            email_id=1,
            lock_id=0,
            flags=0,
            source='Web',
            isoverdue=0,
            isanswered=0,
            sort=0,
            ip_address=request.META.get('REMOTE_ADDR', ''),
            created=timezone.now(),
            updated=timezone.now(),
        )
        ticket.save()
        # TicketCdata
        priority_obj = get_object_or_404(TicketPriority, pk=priority_id)
        cdata = TicketCdata(ticket_id=ticket.ticket_id,
                            subject=subject,
                            priority=priority_obj.priority)
        cdata.save()
        # user message
        entry = ThreadEntry(pid=0,
                            thread_id=ticket.ticket_id,
                            staff_id=0,
                            user_id=user_id,
                            type='M', flags=0,
                            poster=subject,
                            source='Web',
                            title=subject,
                            body=message,
                            format='text',
                            ip_address=request.META.get('REMOTE_ADDR', ''),
                            created=timezone.now(),
                            updated=timezone.now())
        entry.save()
        return redirect('ticket_list')
    # GET: form
    help_topics = HelpTopic.objects.filter(ispublic=1)
    priorities = TicketPriority.objects.all()
    departments = Department.objects.all()
    return render(request, 'ticket_create.html', {
        'help_topics': help_topics,
        'priorities': priorities,
        'departments': departments
    })

def ticket_detail(request, ticket_id):
    user_id = request.session.get('user_id')
    ticket = get_object_or_404(Ticket, ticket_id=ticket_id, user_id=user_id)
    cdata = TicketCdata.objects.get(ticket_id=ticket_id)
    entries = ThreadEntry.objects.filter(thread_id=ticket_id).order_by('created')
    return render(request, 'ticket_detail.html', {
        'ticket': ticket,
        'subject': cdata.subject,
        'created': ticket.created,
        'entries': entries
    })


def ticket_list(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    tickets = Ticket.objects.filter(user_id=user_id).order_by('-created') # d'uh

    # get subject with all tickets
    ticket_data = []
    for t in tickets:
        cdata = TicketCdata.objects.filter(ticket_id=t.ticket_id).first()
        ticket_data.append({
            'ticket': t,
            'subject': cdata.subject if cdata else '(No Subject)',
        })

    return render(request, 'ticket_list.html', {
        'ticket_data': ticket_data
    })


def logout_view(request):
    request.session.flush()
    return redirect('login')

# basic staff control will do
def is_admin(request):
    return request.session.get('staff_id') is not None

# Admin login
def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            staff = Staff.objects.get(username=username, isactive=1)
            if not check_password(password, staff.passwd):
                raise Staff.DoesNotExist
            request.session['staff_id'] = staff.staff_id
            return redirect('admin_ticket_list')
        except Staff.DoesNotExist:
            return render(request, 'staff/login.html', {'error': 'Invalid credentials'})
    return render(request, 'staff/login.html')

# Admin ticket list
def admin_ticket_list(request):
    if not is_admin(request):
        return redirect('admin_login')
    tickets = Ticket.objects.all().order_by('-created')
    ticket_data = []
    for t in tickets:
        cdata = TicketCdata.objects.filter(ticket_id=t.ticket_id).first()
        ticket_data.append({
            'ticket': t,
            'subject': cdata.subject if cdata else '(No Subject)',
        })
    return render(request, 'staff/ticket_list.html', {'ticket_data': ticket_data})

# Admin ticket detail and response
def admin_ticket_detail(request, ticket_id):
    if not is_admin(request):
        return redirect('admin_login')

    ticket = get_object_or_404(Ticket, ticket_id=ticket_id)
    cdata = TicketCdata.objects.filter(ticket_id=ticket_id).first()
    entries = ThreadEntry.objects.filter(thread_id=ticket_id).order_by('created')

    if request.method == 'POST':
        body = request.POST.get('message')
        staff_id = request.session.get('staff_id')
        entry = ThreadEntry(
            pid=0,
            thread_id=ticket_id,
            staff_id=staff_id,
            user_id=0,
            type='R',  # R: Response
            flags=0,
            poster='Admin Response',
            source='Web',
            title='Response',
            body=body,
            format='text',
            ip_address=request.META.get('REMOTE_ADDR', ''),
            created=timezone.now(),
            updated=timezone.now()
        )
        entry.save()
        ticket.isanswered = 1
        ticket.updated = timezone.now()
        ticket.save()
        return redirect('admin_ticket_detail', ticket_id=ticket_id)

    return render(request, 'staff/ticket_detail.html', {
        'ticket': ticket,
        'subject': cdata.subject if cdata else '',
        'entries': entries
    })

# update ticket status
def admin_update_status(request, ticket_id):
    if not is_admin(request):
        return redirect('admin_login')

    ticket = get_object_or_404(Ticket, ticket_id=ticket_id)
    if request.method == 'POST':
        status_id = request.POST.get('status_id')
        ticket.status_id = status_id
        ticket.updated = timezone.now()
        ticket.save()
        return redirect('admin_ticket_detail', ticket_id=ticket_id)

    statuses = TicketStatus.objects.all()
    return render(request, 'staff/update_status.html', {'ticket': ticket, 'statuses': statuses})

def assign_ticket_to_staff(request, ticket_id):
    if not is_admin(request):
        return redirect('admin_login')

    ticket = get_object_or_404(Ticket, ticket_id=ticket_id)
    staff_list = Staff.objects.filter(isactive=1)

    if request.method == 'POST':
        assigned_staff_id = request.POST.get('staff_id')
        ticket.staff_id = assigned_staff_id
        ticket.updated = timezone.now()
        ticket.save()
        return redirect('admin_ticket_detail', ticket_id=ticket_id)

    return render(request, 'staff/assign_ticket.html', {
        'ticket': ticket,
        'staff_list': staff_list
    })

# add attachment
def upload_attachment(request, ticket_id):
    if not is_admin(request):
        return redirect('admin_login')

    ticket = get_object_or_404(Ticket, ticket_id=ticket_id)

    if request.method == 'POST' and request.FILES['file']:
        upload = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(upload.name, upload)
        Attachment.objects.create(
            ticket_id=ticket_id,
            file_path=filename,
            name=upload.name,
            type=upload.content_type,
            size=upload.size,
            created=timezone.now()
        )
        return redirect('admin_ticket_detail', ticket_id=ticket_id)

    return render(request, 'staff/upload_attachment.html', {
        'ticket': ticket
    })