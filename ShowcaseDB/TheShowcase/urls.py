from ShowcaseDB.urls import path
from django.urls import path
from .views import main_views, employee_views, mentor_views

urlpatterns = [
    #Main Paths
    path('', main_views.home, name="home"),

    #Employee Paths
    path('employee/signup/', employee_views.employee_signup, name="employee_signup"),
    path('employee/signup/form', employee_views.employee_signup_form, name="employee_signup_form"),
    path('employee/login/', employee_views.employee_login, name='employee_login'),
    path('employee/forgotpassword', employee_views.employee_forgotPassword, name='employee_forgot_password'),
    path('employee/resetpassword', employee_views.employee_resetPassword, name="employee_reset_password"),
    path('employee/resetpassword/submission', employee_views.employee_resetPassword_Submission, name="employee_resetPassword_Submission"),


    #Temp Employee Paths
    path('employee/login/successful', employee_views.employee_login_successful, name='employee_login_successful'),
    path('employee/signup/summary/', employee_views.employee_signup_form_submission, name="employee_signup_submission"),

    #Mentor Paths
    path('mentor/signup', mentor_views.mentor_signup, name='mentor_signup'),
    path('mentor/signup/form', mentor_views.mentor_signup_form , name="mentor_signup_form"),

    
]
