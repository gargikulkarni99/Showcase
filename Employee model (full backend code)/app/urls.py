from django.urls import path
from . import views

## TODO: add all other login/signup paths
urlpatterns = [
    path('employees-login', views.employees_login, name='employees-login'),
    path('forgot-password-employees', views.employees_forgot_password, name='forgot-password-employees'),
    path('employees-signup-step1', views.employees_signup_step1, name='employees-signup-step1'),
    path('employees-signup-step2', views.employees_signup_step2, name='employees-signup-step2')
]