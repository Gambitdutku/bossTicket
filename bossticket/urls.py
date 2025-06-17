from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('ticket/create/', views.create_ticket, name='create_ticket'),
    path('ticket/<int:ticket_id>/', views.ticket_detail, name='ticket_detail'),
    path('ticket/list/', views.ticket_list, name='ticket_list'),
    path('staff/login/', views.admin_login, name='admin_login'),
    path('staff/tickets/', views.admin_ticket_list, name='admin_ticket_list'),
    path('staff/ticket/<int:ticket_id>/', views.admin_ticket_detail, name='admin_ticket_detail'),
    path('staff/ticket/<int:ticket_id>/status/', views.admin_update_status, name='admin_update_status'),
    path('staff/ticket/<int:ticket_id>/assign/', views.assign_ticket_to_staff, name='assign_ticket_to_staff'),
    path('staff/ticket/<int:ticket_id>/upload/', views.upload_attachment, name='upload_attachment'),
]
