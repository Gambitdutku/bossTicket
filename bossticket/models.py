from django.db import models

class TicketPriority(models.Model):
    priority_id = models.SmallIntegerField(primary_key=True)
    priority = models.CharField(max_length=60)
    priority_desc = models.CharField(max_length=30)
    priority_color = models.CharField(max_length=7)
    priority_urgency = models.PositiveSmallIntegerField(default=0)
    ispublic = models.BooleanField(default=True)

    class Meta:
        managed = False
        db_table = 'ost_ticket_priority'

class TicketStatus(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    state = models.CharField(max_length=16, null=True, blank=True)
    mode = models.PositiveIntegerField(default=0)
    flags = models.PositiveIntegerField(default=0)
    sort = models.PositiveIntegerField(default=0)
    properties = models.TextField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_ticket_status'

class Ticket(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    ticket_pid = models.PositiveIntegerField(null=True, blank=True)
    number = models.CharField(max_length=20, null=True, blank=True)
    user = models.ForeignKey('User', models.CASCADE, db_column='user_id')
    user_email = models.ForeignKey('UserEmail', models.CASCADE, db_column='user_email_id')
    status = models.ForeignKey(TicketStatus, models.CASCADE, db_column='status_id')
    dept = models.ForeignKey('Department', models.CASCADE, db_column='dept_id')
    sla = models.ForeignKey('Sla', models.CASCADE, db_column='sla_id')
    topic = models.ForeignKey('HelpTopic', models.CASCADE, db_column='topic_id')
    staff = models.ForeignKey('Staff', models.CASCADE, db_column='staff_id')
    team = models.ForeignKey('Team', models.CASCADE, db_column='team_id')
    email = models.ForeignKey('Email', models.CASCADE, db_column='email_id')
    lock = models.ForeignKey('Lock', models.CASCADE, db_column='lock_id')
    flags = models.PositiveIntegerField(default=0)
    sort = models.PositiveIntegerField(default=0)
    ip_address = models.CharField(max_length=64, default='')
    source = models.CharField(max_length=5, choices=[('Web','Web'),('Email','Email'),('Phone','Phone'),('API','API'),('Other','Other')], default='Other')
    source_extra = models.CharField(max_length=40, null=True, blank=True)
    isoverdue = models.BooleanField(default=False)
    isanswered = models.BooleanField(default=False)
    duedate = models.DateTimeField(null=True, blank=True)
    est_duedate = models.DateTimeField(null=True, blank=True)
    reopened = models.DateTimeField(null=True, blank=True)
    closed = models.DateTimeField(null=True, blank=True)
    lastupdate = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_ticket'

class TicketCData(models.Model):
    ticket = models.OneToOneField(Ticket, models.CASCADE, primary_key=True, db_column='ticket_id')
    subject = models.TextField(null=True, blank=True)
    priority = models.TextField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'ost_ticket__cdata'

class Thread(models.Model):
    id = models.AutoField(primary_key=True)
    object_id = models.PositiveIntegerField()
    object_type = models.CharField(max_length=1)
    extra = models.TextField(null=True, blank=True)
    lastresponse = models.DateTimeField(null=True, blank=True)
    lastmessage = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_thread'

class ThreadCollaborator(models.Model):
    id = models.AutoField(primary_key=True)
    flags = models.PositiveIntegerField(default=1)
    thread = models.ForeignKey(Thread, models.CASCADE, db_column='thread_id')
    user = models.ForeignKey('User', models.CASCADE, db_column='user_id')
    role = models.CharField(max_length=1, default='M')
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_thread_collaborator'

class ThreadEntry(models.Model):
    id = models.AutoField(primary_key=True)
    pid = models.PositiveIntegerField(default=0)
    thread = models.ForeignKey(Thread, models.CASCADE, db_column='thread_id')
    staff = models.ForeignKey('Staff', models.CASCADE, db_column='staff_id')
    user = models.ForeignKey('User', models.CASCADE, db_column='user_id')
    type = models.CharField(max_length=1, default='')
    flags = models.PositiveIntegerField(default=0)
    poster = models.CharField(max_length=128, default='')
    editor = models.PositiveIntegerField(null=True, blank=True)
    editor_type = models.CharField(max_length=1, null=True, blank=True)
    source = models.CharField(max_length=32, default='')
    title = models.CharField(max_length=255, null=True, blank=True)
    body = models.TextField()
    format = models.CharField(max_length=16, default='html')
    ip_address = models.CharField(max_length=64, default='')
    extra = models.TextField(null=True, blank=True)
    recipients = models.TextField(null=True, blank=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_thread_entry'

class ThreadEntryEmail(models.Model):
    id = models.AutoField(primary_key=True)
    thread_entry = models.ForeignKey(ThreadEntry, models.CASCADE, db_column='thread_entry_id')
    email = models.ForeignKey('Email', models.CASCADE, db_column='email_id', null=True)
    mid = models.CharField(max_length=255)
    headers = models.TextField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'ost_thread_entry_email'

class ThreadEntryMerge(models.Model):
    id = models.AutoField(primary_key=True)
    thread_entry = models.ForeignKey(ThreadEntry, models.CASCADE, db_column='thread_entry_id')
    data = models.TextField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'ost_thread_entry_merge'

class ThreadEvent(models.Model):
    id = models.AutoField(primary_key=True)
    thread = models.ForeignKey(Thread, models.CASCADE, db_column='thread_id')
    thread_type = models.CharField(max_length=1, default='')
    event = models.ForeignKey('Event', models.CASCADE, db_column='event_id', null=True, blank=True)
    staff = models.ForeignKey('Staff', models.CASCADE, db_column='staff_id')
    team = models.ForeignKey('Team', models.CASCADE, db_column='team_id')
    dept = models.ForeignKey('Department', models.CASCADE, db_column='dept_id')
    topic = models.ForeignKey('HelpTopic', models.CASCADE, db_column='topic_id')
    data = models.CharField(max_length=1024, null=True, blank=True)  # Encoded differences
    username = models.CharField(max_length=128, default='SYSTEM')
    uid = models.PositiveIntegerField(null=True, blank=True)
    uid_type = models.CharField(max_length=1, default='S')
    annulled = models.BooleanField(default=False)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_thread_event'

class ThreadReferral(models.Model):
    id = models.AutoField(primary_key=True)
    thread = models.ForeignKey(Thread, models.CASCADE, db_column='thread_id')
    object_id = models.PositiveIntegerField()
    object_type = models.CharField(max_length=1)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_thread_referral'
class Email(models.Model):
    email_id = models.AutoField(primary_key=True)
    noautoresp = models.BooleanField(default=False)
    priority = models.ForeignKey(TicketPriority, models.CASCADE, db_column='priority_id')
    dept = models.ForeignKey('Department', models.CASCADE, db_column='dept_id')
    topic = models.ForeignKey('HelpTopic', models.CASCADE, db_column='topic_id')
    email = models.CharField(max_length=255, default='')
    name = models.CharField(max_length=255, default='')
    notes = models.TextField(null=True, blank=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_email'

class EmailAccount(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.ForeignKey(Email, models.CASCADE, db_column='email_id')
    type = models.CharField(max_length=7, choices=[('mailbox','mailbox'),('smtp','smtp')], default='mailbox')
    auth_bk = models.CharField(max_length=128)
    auth_id = models.CharField(max_length=16, null=True, blank=True)
    active = models.BooleanField(default=False)
    host = models.CharField(max_length=128, default='')
    port = models.IntegerField()
    folder = models.CharField(max_length=255, null=True, blank=True)
    protocol = models.CharField(max_length=5, choices=[('IMAP','IMAP'),('POP','POP'),('SMTP','SMTP'),('OTHER','OTHER')], default='OTHER')
    encryption = models.CharField(max_length=4, choices=[('NONE','NONE'),('AUTO','AUTO'),('SSL','SSL')], default='AUTO')
    fetchfreq = models.PositiveSmallIntegerField(default=5)
    fetchmax = models.PositiveSmallIntegerField(default=30)
    postfetch = models.CharField(max_length=7, choices=[('archive','archive'),('delete','delete'),('nothing','nothing')], default='nothing')
    archivefolder = models.CharField(max_length=255, null=True, blank=True)
    allow_spoofing = models.BooleanField(default=False)
    num_errors = models.PositiveIntegerField(default=0)
    last_error_msg = models.TextField(null=True, blank=True)
    last_error = models.DateTimeField(null=True, blank=True)
    last_activity = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_email_account'

class EmailTemplate(models.Model):
    id = models.AutoField(primary_key=True)
    tpl_id = models.PositiveIntegerField()
    code_name = models.CharField(max_length=32)
    subject = models.CharField(max_length=255, default='')
    body = models.TextField()
    notes = models.TextField(null=True, blank=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_email_template'

class EmailTemplateGroup(models.Model):
    tpl_id = models.AutoField(primary_key=True)
    isactive = models.BooleanField(default=False)
    name = models.CharField(max_length=32, default='')
    lang = models.CharField(max_length=16, default='en_US')
    notes = models.TextField(null=True, blank=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_email_template_group'
class Filter(models.Model):
    id = models.AutoField(primary_key=True)
    execorder = models.PositiveIntegerField(default=99)
    isactive = models.BooleanField(default=True)
    flags = models.PositiveIntegerField(default=0)
    status = models.PositiveIntegerField(default=0)
    match_all_rules = models.BooleanField(default=False)
    stop_onmatch = models.BooleanField(default=False)
    target = models.CharField(max_length=5, choices=[('Any','Any'),('Web','Web'),('Email','Email'),('API','API')], default='Any')
    email = models.ForeignKey(Email, models.CASCADE, db_column='email_id')
    name = models.CharField(max_length=32, default='')
    notes = models.TextField(null=True, blank=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_filter'

class FilterAction(models.Model):
    id = models.AutoField(primary_key=True)
    filter = models.ForeignKey(Filter, models.CASCADE, db_column='filter_id')
    sort = models.PositiveIntegerField(default=0)
    type = models.CharField(max_length=24)
    configuration = models.TextField(null=True, blank=True)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_filter_action'

class FilterRule(models.Model):
    id = models.AutoField(primary_key=True)
    filter = models.ForeignKey(Filter, models.CASCADE, db_column='filter_id')
    what = models.CharField(max_length=32)
    how = models.CharField(max_length=10, choices=[
        ('equal','equal'),('not_equal','not_equal'),('contains','contains'),
        ('dn_contain','dn_contain'),('starts','starts'),('ends','ends'),
        ('match','match'),('not_match','not_match')
    ])
    val = models.CharField(max_length=255)
    isactive = models.BooleanField(default=True)
    notes = models.TextField(null=True, blank=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_filter_rule'
class Form(models.Model):
    id = models.AutoField(primary_key=True)
    pid = models.PositiveIntegerField(null=True, blank=True)
    type = models.CharField(max_length=8, default='G')
    flags = models.PositiveIntegerField(default=1)
    title = models.CharField(max_length=255)
    instructions = models.CharField(max_length=512, null=True, blank=True)
    name = models.CharField(max_length=64, default='')
    notes = models.TextField(null=True, blank=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_form'

class FormEntry(models.Model):
    id = models.AutoField(primary_key=True)
    form = models.ForeignKey(Form, models.CASCADE, db_column='form_id')
    object_id = models.PositiveIntegerField(null=True, blank=True)
    object_type = models.CharField(max_length=1, default='T')
    sort = models.PositiveIntegerField(default=1)
    extra = models.TextField(null=True, blank=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_form_entry'

class FormEntryValues(models.Model):
    entry = models.ForeignKey(FormEntry, models.CASCADE, db_column='entry_id')
    field = models.ForeignKey('FormField', models.CASCADE, db_column='field_id')
    value = models.TextField(null=True, blank=True)
    value_id = models.IntegerField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'ost_form_entry_values'

class FormField(models.Model):
    id = models.AutoField(primary_key=True)
    form = models.ForeignKey(Form, models.CASCADE, db_column='form_id')
    flags = models.PositiveIntegerField(default=1)
    type = models.CharField(max_length=255, default='text')
    label = models.CharField(max_length=255)
    name = models.CharField(max_length=64)
    configuration = models.TextField(null=True, blank=True)
    sort = models.PositiveIntegerField()
    hint = models.CharField(max_length=512, null=True, blank=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_form_field'

class HelpTopic(models.Model):
    topic_id = models.AutoField(primary_key=True)
    topic_pid = models.PositiveIntegerField(default=0)
    ispublic = models.BooleanField(default=True)
    noautoresp = models.BooleanField(default=False)
    flags = models.PositiveIntegerField(default=0)
    status = models.ForeignKey(TicketStatus, models.CASCADE, db_column='status_id')
    priority = models.ForeignKey(TicketPriority, models.CASCADE, db_column='priority_id')
    dept = models.ForeignKey('Department', models.CASCADE, db_column='dept_id')
    staff = models.ForeignKey('Staff', models.CASCADE, db_column='staff_id')
    team = models.ForeignKey('Team', models.CASCADE, db_column='team_id')
    sla = models.ForeignKey('Sla', models.CASCADE, db_column='sla_id')
    page_id = models.PositiveIntegerField(default=0)
    sequence_id = models.PositiveIntegerField(default=0)
    sort = models.PositiveIntegerField(default=0)
    topic = models.CharField(max_length=128, default='')
    number_format = models.CharField(max_length=32, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_help_topic'

class HelpTopicForm(models.Model):
    id = models.AutoField(primary_key=True)
    topic = models.ForeignKey(HelpTopic, models.CASCADE, db_column='topic_id')
    form = models.ForeignKey(Form, models.CASCADE, db_column='form_id')
    sort = models.PositiveIntegerField(default=1)
    extra = models.TextField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'ost_help_topic_form'
class FAQ(models.Model):
    faq_id = models.AutoField(primary_key=True)
    category = models.ForeignKey('FAQCategory', models.CASCADE, db_column='category_id')
    ispublished = models.BooleanField(default=False)
    question = models.CharField(max_length=255)
    answer = models.TextField()
    keywords = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_faq'

class FAQCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_pid = models.PositiveIntegerField(null=True, blank=True)
    ispublic = models.BooleanField(default=False)
    name = models.CharField(max_length=125, null=True, blank=True)
    description = models.TextField()
    notes = models.TextField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_faq_category'

class FAQTopic(models.Model):
    faq = models.ForeignKey(FAQ, models.CASCADE, db_column='faq_id')
    topic = models.ForeignKey(HelpTopic, models.CASCADE, db_column='topic_id')

    class Meta:
        managed = False
        db_table = 'ost_faq_topic'
class List(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    name_plural = models.CharField(max_length=255, null=True, blank=True)
    sort_mode = models.CharField(max_length=8, choices=[('Alpha','Alpha'),('-Alpha','-Alpha'),('SortCol','SortCol')], default='Alpha')
    masks = models.PositiveIntegerField(default=0)
    type = models.CharField(max_length=16, null=True, blank=True)
    configuration = models.TextField()
    notes = models.TextField(null=True, blank=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_list'

class ListItem(models.Model):
    id = models.AutoField(primary_key=True)
    list = models.ForeignKey(List, models.CASCADE, db_column='list_id', null=True)
    status = models.PositiveIntegerField(default=1)
    value = models.CharField(max_length=255)
    extra = models.CharField(max_length=255, null=True, blank=True)
    sort = models.IntegerField(default=1)
    properties = models.TextField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'ost_list_items'
class Lock(models.Model):
    lock_id = models.AutoField(primary_key=True)
    staff = models.ForeignKey('Staff', models.CASCADE, db_column='staff_id')
    expire = models.DateTimeField(null=True, blank=True)
    code = models.CharField(max_length=20, null=True, blank=True)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_lock'

class Note(models.Model):
    id = models.AutoField(primary_key=True)
    pid = models.PositiveIntegerField(null=True, blank=True)
    staff = models.ForeignKey('Staff', models.CASCADE, db_column='staff_id')
    ext_id = models.CharField(max_length=10, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    status = models.PositiveIntegerField(default=0)
    sort = models.PositiveIntegerField(default=0)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_note'

class CannedResponse(models.Model):
    canned_id = models.AutoField(primary_key=True)
    dept = models.ForeignKey('Department', models.CASCADE, db_column='dept_id')
    isenabled = models.BooleanField(default=True)
    title = models.CharField(max_length=255, default='')
    response = models.TextField()
    lang = models.CharField(max_length=16, default='en_US')
    notes = models.TextField(null=True, blank=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_canned_response'

class Content(models.Model):
    id = models.AutoField(primary_key=True)
    isactive = models.BooleanField(default=False)
    type = models.CharField(max_length=32, default='other')
    name = models.CharField(max_length=255)
    body = models.TextField()
    notes = models.TextField(null=True, blank=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_content'

class Config(models.Model):
    id = models.AutoField(primary_key=True)
    namespace = models.CharField(max_length=64)
    key = models.CharField(max_length=64)
    value = models.TextField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_config'
class Queue(models.Model):
    id = models.AutoField(primary_key=True)
    parent_id = models.PositiveIntegerField(default=0)
    columns_id = models.PositiveIntegerField(null=True, blank=True)
    sort_id = models.PositiveIntegerField(null=True, blank=True)
    flags = models.PositiveIntegerField(default=0)
    staff = models.ForeignKey('Staff', models.CASCADE, db_column='staff_id')
    sort = models.PositiveIntegerField(default=0)
    title = models.CharField(max_length=60, null=True, blank=True)
    config = models.TextField(null=True, blank=True)
    filter = models.CharField(max_length=64, null=True, blank=True)
    root = models.CharField(max_length=32, null=True, blank=True)
    path = models.CharField(max_length=80, default='/')
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_queue'

class QueueColumn(models.Model):
    id = models.AutoField(primary_key=True)
    flags = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=64, default='')
    primary = models.CharField(max_length=64, default='')
    secondary = models.CharField(max_length=64, null=True, blank=True)
    filter = models.CharField(max_length=32, null=True, blank=True)
    truncate = models.CharField(max_length=16, null=True, blank=True)
    annotations = models.TextField(null=True, blank=True)
    conditions = models.TextField(null=True, blank=True)
    extra = models.TextField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'ost_queue_column'

class QueueColumns(models.Model):
    queue = models.ForeignKey(Queue, models.CASCADE, db_column='queue_id')
    column = models.ForeignKey(QueueColumn, models.CASCADE, db_column='column_id')
    staff = models.ForeignKey('Staff', models.CASCADE, db_column='staff_id')
    bits = models.PositiveIntegerField(default=0)
    sort = models.PositiveIntegerField(default=1)
    heading = models.CharField(max_length=64, null=True, blank=True)
    width = models.PositiveIntegerField(default=100)

    class Meta:
        managed = False
        db_table = 'ost_queue_columns'

class QueueConfig(models.Model):
    queue = models.ForeignKey(Queue, models.CASCADE, db_column='queue_id')
    staff = models.ForeignKey('Staff', models.CASCADE, db_column='staff_id')
    setting = models.TextField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_queue_config'

class QueueExport(models.Model):
    id = models.AutoField(primary_key=True)
    queue = models.ForeignKey(Queue, models.CASCADE, db_column='queue_id')
    path = models.CharField(max_length=64, default='')
    heading = models.CharField(max_length=64, null=True, blank=True)
    sort = models.PositiveIntegerField(default=1)

    class Meta:
        managed = False
        db_table = 'ost_queue_export'

class QueueSort(models.Model):
    id = models.AutoField(primary_key=True)
    root = models.CharField(max_length=32, null=True, blank=True)
    name = models.CharField(max_length=64, default='')
    columns = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'ost_queue_sort'

class QueueSorts(models.Model):
    queue = models.ForeignKey(Queue, models.CASCADE, db_column='queue_id')
    sort = models.ForeignKey(QueueSort, models.CASCADE, db_column='sort_id')
    bits = models.PositiveIntegerField(default=0)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        managed = False
        db_table = 'ost_queue_sorts'
class Organization(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, default='')
    manager = models.CharField(max_length=16, default='')
    status = models.PositiveIntegerField(default=0)
    domain = models.CharField(max_length=256, default='')
    extra = models.TextField(null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)
    updated = models.DateTimeField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'ost_organization'

class OrganizationCData(models.Model):
    org = models.OneToOneField(Organization, models.CASCADE, primary_key=True, db_column='org_id')
    name = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    phone = models.TextField(null=True, blank=True)
    website = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'ost_organization__cdata'

class User(models.Model):
    id = models.AutoField(primary_key=True)
    org = models.ForeignKey(Organization, models.CASCADE, db_column='org_id')
    default_email = models.ForeignKey('UserEmail', models.CASCADE, db_column='default_email_id')
    status = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=128)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_user'

class UserAccount(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.CASCADE, db_column='user_id')
    status = models.PositiveIntegerField(default=0)
    timezone = models.CharField(max_length=64, null=True, blank=True)
    lang = models.CharField(max_length=16, null=True, blank=True)
    username = models.CharField(max_length=64, null=True, blank=True)
    passwd = models.CharField(max_length=128, null=True, blank=True)
    backend = models.CharField(max_length=32, null=True, blank=True)
    extra = models.TextField(null=True, blank=True)
    registered = models.DateTimeField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'ost_user_account'

class UserEmail(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.CASCADE, db_column='user_id')
    flags = models.PositiveIntegerField(default=0)
    address = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ost_user_email'

class UserCData(models.Model):
    user = models.OneToOneField(User, models.CASCADE, primary_key=True, db_column='user_id')
    email = models.TextField(null=True, blank=True)
    name = models.TextField(null=True, blank=True)
    phone = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'ost_user__cdata'
class Role(models.Model):
    id = models.AutoField(primary_key=True)
    flags = models.PositiveIntegerField(default=1)
    name = models.CharField(max_length=64, null=True, blank=True)
    permissions = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_role'

class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    dept = models.ForeignKey('Department', models.CASCADE, db_column='dept_id')
    role = models.ForeignKey(Role, models.CASCADE, db_column='role_id')
    username = models.CharField(max_length=32, unique=True)
    firstname = models.CharField(max_length=32, null=True, blank=True)
    lastname = models.CharField(max_length=32, null=True, blank=True)
    passwd = models.CharField(max_length=128, null=True, blank=True)
    backend = models.CharField(max_length=32, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=24, default='')
    phone_ext = models.CharField(max_length=6, null=True, blank=True)
    mobile = models.CharField(max_length=24, default='')
    signature = models.TextField(null=True, blank=True)
    lang = models.CharField(max_length=16, null=True, blank=True)
    timezone = models.CharField(max_length=64, null=True, blank=True)
    locale = models.CharField(max_length=16, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    isactive = models.BooleanField(default=True)
    isadmin = models.BooleanField(default=False)
    isvisible = models.BooleanField(default=True)
    onvacation = models.BooleanField(default=False)
    assigned_only = models.BooleanField(default=False)
    show_assigned_tickets = models.BooleanField(default=False)
    change_passwd = models.BooleanField(default=False)
    max_page_size = models.PositiveIntegerField(default=0)
    auto_refresh_rate = models.PositiveIntegerField(default=0)
    default_signature_type = models.CharField(max_length=6, choices=[('none','none'),('mine','mine'),('dept','dept')], default='none')
    default_paper_size = models.CharField(max_length=6, choices=[('Letter','Letter'),('Legal','Legal'),('Ledger','Ledger'),('A4','A4'),('A3','A3')], default='Letter')
    extra = models.TextField(null=True, blank=True)
    permissions = models.TextField(null=True, blank=True)
    created = models.DateTimeField()
    lastlogin = models.DateTimeField(null=True, blank=True)
    passwdreset = models.DateTimeField(null=True, blank=True)
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_staff'

class StaffDeptAccess(models.Model):
    staff = models.ForeignKey(Staff, models.CASCADE, db_column='staff_id')
    dept = models.ForeignKey('Department', models.CASCADE, db_column='dept_id')
    role = models.ForeignKey(Role, models.CASCADE, db_column='role_id')
    flags = models.PositiveIntegerField(default=1)

    class Meta:
        managed = False
        db_table = 'ost_staff_dept_access'

class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    lead = models.ForeignKey(Staff, models.CASCADE, db_column='lead_id')
    flags = models.PositiveIntegerField(default=1)
    name = models.CharField(max_length=125, default='')
    notes = models.TextField(null=True, blank=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_team'

class TeamMember(models.Model):
    team = models.ForeignKey(Team, models.CASCADE, db_column='team_id')
    staff = models.ForeignKey(Staff, models.CASCADE, db_column='staff_id')
    flags = models.PositiveIntegerField(default=0)

    class Meta:
        managed = False
        db_table = 'ost_team_member'
class APIKey(models.Model):
    id = models.AutoField(primary_key=True)
    isactive = models.BooleanField(default=True)
    ipaddr = models.CharField(max_length=64)
    apikey = models.CharField(max_length=255, unique=True)
    can_create_tickets = models.BooleanField(default=True)
    can_exec_cron = models.BooleanField(default=True)
    notes = models.TextField(null=True, blank=True)
    updated = models.DateTimeField()
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_api_key'

class Attachment(models.Model):
    id = models.AutoField(primary_key=True)
    object_id = models.PositiveIntegerField()
    type = models.CharField(max_length=1)
    file = models.ForeignKey('File', models.CASCADE, db_column='file_id')
    name = models.CharField(max_length=255, null=True, blank=True)
    inline = models.BooleanField(default=False)
    lang = models.CharField(max_length=16, null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'ost_attachment'

class Department(models.Model):
    id = models.AutoField(primary_key=True)
    pid = models.PositiveIntegerField(null=True, blank=True)
    tpl_id = models.PositiveIntegerField(default=0)
    sla = models.ForeignKey('Sla', models.CASCADE, db_column='sla_id')
    schedule = models.ForeignKey('Schedule', models.CASCADE, db_column='schedule_id')
    email = models.ForeignKey(Email, models.CASCADE, db_column='email_id')
    autoresp_email = models.ForeignKey(Email, models.CASCADE, db_column='autoresp_email_id')
    manager = models.ForeignKey(Staff, models.CASCADE, db_column='manager_id')
    flags = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=128, default='')
    signature = models.TextField()
    ispublic = models.BooleanField(default=True)
    group_membership = models.BooleanField(default=False)
    ticket_auto_response = models.BooleanField(default=True)
    message_auto_response = models.BooleanField(default=False)
    path = models.CharField(max_length=128, default='/')
    updated = models.DateTimeField()
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_department'

class Draft(models.Model):
    id = models.AutoField(primary_key=True)
    staff = models.ForeignKey(Staff, models.CASCADE, db_column='staff_id')
    namespace = models.CharField(max_length=32, default='')
    body = models.TextField()
    extra = models.TextField(null=True, blank=True)
    created = models.DateTimeField()
    updated = models.DateTimeField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'ost_draft'

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=60, null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'ost_event'

class File(models.Model):
    id = models.AutoField(primary_key=True)
    ft = models.CharField(max_length=1, default='T')
    bk = models.CharField(max_length=1, default='D')
    type = models.CharField(max_length=255, default='')
    size = models.PositiveBigIntegerField(default=0)
    key = models.CharField(max_length=86)
    signature = models.CharField(max_length=86)
    name = models.CharField(max_length=255, default='')
    attrs = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_file'

class FileChunk(models.Model):
    file = models.ForeignKey(File, models.CASCADE, db_column='file_id')
    chunk_id = models.IntegerField()
    filedata = models.BinaryField()

    class Meta:
        managed = False
        db_table = 'ost_file_chunk'

class Group(models.Model):
    id = models.AutoField(primary_key=True)
    role = models.ForeignKey(Role, models.CASCADE, db_column='role_id')
    flags = models.PositiveIntegerField(default=1)
    name = models.CharField(max_length=120, default='')
    notes = models.TextField(null=True, blank=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_group'

class Plugin(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    install_path = models.CharField(max_length=60)
    isphar = models.BooleanField(default=False)
    isactive = models.BooleanField(default=False)
    version = models.CharField(max_length=64, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    installed = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_plugin'

class PluginInstance(models.Model):
    id = models.AutoField(primary_key=True)
    plugin = models.ForeignKey(Plugin, models.CASCADE, db_column='plugin_id')
    flags = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=255, default='')
    notes = models.TextField(null=True, blank=True)
    created = models.DateTimeField()
    updated = models.DateTimeField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'ost_plugin_instance'

class Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    flags = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=255)
    timezone = models.CharField(max_length=64, null=True, blank=True)
    description = models.CharField(max_length=255)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_schedule'

class ScheduleEntry(models.Model):
    id = models.AutoField(primary_key=True)
    schedule = models.ForeignKey(Schedule, models.CASCADE, db_column='schedule_id')
    flags = models.PositiveIntegerField(default=0)
    sort = models.PositiveSmallIntegerField(default=0)
    name = models.CharField(max_length=255)
    repeats = models.CharField(max_length=16, default='never')
    starts_on = models.DateField(null=True, blank=True)
    starts_at = models.TimeField(null=True, blank=True)
    ends_on = models.DateField(null=True, blank=True)
    ends_at = models.TimeField(null=True, blank=True)
    stops_on = models.DateTimeField(null=True, blank=True)
    day = models.PositiveSmallIntegerField(null=True, blank=True)
    week = models.PositiveSmallIntegerField(null=True, blank=True)
    month = models.PositiveSmallIntegerField(null=True, blank=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_schedule_entry'

class Sequence(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, null=True, blank=True)
    flags = models.PositiveIntegerField(null=True, blank=True)
    next = models.PositiveBigIntegerField(default=1)
    increment = models.IntegerField(default=1)
    padding = models.CharField(max_length=1, default='0')
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_sequence'

class Session(models.Model):
    session_id = models.CharField(max_length=255, primary_key=True)
    session_data = models.BinaryField(null=True, blank=True)
    session_expire = models.DateTimeField(null=True, blank=True)
    session_updated = models.DateTimeField(null=True, blank=True)
    user_id = models.CharField(max_length=16, default='0')  # osTicket staff/client ID
    user_ip = models.CharField(max_length=64)
    user_agent = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ost_session'

class Sla(models.Model):
    id = models.AutoField(primary_key=True)
    schedule = models.ForeignKey(Schedule, models.CASCADE, db_column='schedule_id')
    flags = models.PositiveIntegerField(default=3)
    grace_period = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=64, default='')
    notes = models.TextField(null=True, blank=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_sla'

class Syslog(models.Model):
    log_id = models.AutoField(primary_key=True)
    log_type = models.CharField(max_length=7, choices=[('Debug','Debug'),('Warning','Warning'),('Error','Error')])
    title = models.CharField(max_length=255)
    log = models.TextField()
    logger = models.CharField(max_length=64)
    ip_address = models.CharField(max_length=64)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ost_syslog'

class Search(models.Model):
    object_type = models.CharField(max_length=8)
    object_id = models.PositiveIntegerField()
    title = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'ost__search'
