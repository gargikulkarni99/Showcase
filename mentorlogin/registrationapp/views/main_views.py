from django.shortcuts import render, redirect
from ..models import Mentor
# from .mentor_views import * is already being imported in init file

# Create your views here.
def home(request) :
    all_mentor = Mentor.objects.all
    return render(request, 'home.html', {'all_mentor':all_mentor})



