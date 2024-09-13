from django.shortcuts import render, redirect
from ..models import Employee, Mentor
# from .employee_views import * is already being imported in init file

# Create your views here.
def home(request) :
    all_employees = Employee.objects.all
    all_mentors = Mentor.objects.all
    return render(request, 'home.html', {
            'all_employees':all_employees,
            'all_mentors': all_mentors,
        })



