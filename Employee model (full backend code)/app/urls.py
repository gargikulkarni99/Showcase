from django.urls import path
from . import views

## TODO: add all other login/signup paths
urlpatterns = [
    path('employees-login', views.employees_login, name='employees-login'),
    path('employees-signup-step1', views.employees_signup_step1, name='employees-signup-step1'),
    path('employees-signup-step2', views.employees_signup_step2, name='employees-signup-step2'),
    path('employees-forgot-step1', views.employees_forgot_step1, name='employees-forgot-step1'),
    path('employees-forgot-step2', views.employees_forgot_step2, name='employees-forgot-step2')
]