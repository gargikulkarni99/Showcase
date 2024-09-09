from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
import psycopg2
import os
from django.core.mail import send_mail
from .models import Employee
import datetime
import uuid
import smtplib
# from config import load_config

## TODO: add all other login/signup views
def employees_login(request):

    # CHECK AGAINST DB
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        users = Employee.objects.raw(f"select id from app_employee where email = '{email}' and password_hash = '{password}'")

        if(len(users) > 0):
            messages.info(request, 'Successfully logged in!')
            print('Successfully logged in!')
            return redirect('employees-login')
        

        messages.info(request, 'Error: invalid username or password.')
        print('Error: invalid email or password.')
        return redirect('employees-login')

    return render(request, 'employees-login.html', {})

def employees_forgot_password(request):
    return render(request, 'forgot-password-employees.html', {})

# mentors, professionals, student, university
def employees_signup_step1(request):
    
    if request.method == 'POST':
        request.session['email'] = request.POST.get('email')
        request.session['university'] = request.POST.get('university')
        print('email:', request.session['email'])
        print('university:', request.session['university'])

        return redirect('employees-signup-step2')

    return render(request, 'employees-signup.html', {})

def employees_signup_step2(request):
    # INSERT INTO DB

    if request.method == 'POST':
        print('Sending mail...')
        print(request.session['email'])

        # # send an email to the user with the static password and a link to redirect to the login page
        # subject='Getting started with The Showcase!'
        # message = 'Welcome to The Showcase! Paste this URL [localhost:8000/employees-login] into your search bar and access via your email. Your auto-generated password is: 12345'
        # from_email = 'showcaseexchangeittest@gmail.com'
        # receiver= [request.session['email']]

        # send_mail(
        #     subject,
        #     message,
        #     from_email,
        #     receiver,
        #     fail_silently=False
        # )

        # put things into the database
        # *currently no university field in the Users model
        email = request.session['email']
        password = request.POST.get('password')
        university = request.session['university']
        first = request.POST.get('firstname')
        last = request.POST.get('lastname')
        phone = request.POST.get('phone')
        dob = request.POST.get('dateofbirth')
        location = request.POST.get('location')
        company = request.POST.get('company')

        if(password == request.POST.get('password2')):

            new_entry = Employee(
                user='new_user', 
                password_hash=password, 
                first_name=first, 
                last_name=last,
                email=email,
                user_type='Employee',
                user_phone=phone,
                user_birthdate=dob,
                company=company
                )

            new_entry.save()
        else:
            print("Error: Passwords don't match")

    return render(request, 'employees-signup-1.html', {})