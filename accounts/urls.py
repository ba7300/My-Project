from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('forgot', views.forgot, name='forgot'),
    path('forgot1', views.forgot1, name='forgot1'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('attendance', views.attendance, name='attendance'),
    path('emp_details', views.emp_details, name='emp_details'),
    path('loans', views.loans, name='loans'),
    path('payslip', views.payslip, name='payslip'),
    path('privacy', views.privacy, name='privacy'),
    path('terms', views.terms, name='terms'),

]
