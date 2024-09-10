from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from ..models import Employee
from django.contrib.auth import authenticate, login

def employee_signup(request) :
    return render(request,'employees-signup.html', {})

def employee_signup_form(request):
    if request.method == 'POST':

        university = request.POST.get('university')
        email = request.POST.get('email')

        # Process data or save to session if needed
        request.session['university'] = university
        request.session['email'] = email

        # Render the next page with the data
        return render(request, 'employees-signup-1.html', 
            {
            'university': university,
            'email': email
        })
    else:
        # Redirect or handle non-POST requests
        return redirect('employee_signup')
    
def employee_signup_form_submission(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        date_of_birth = request.POST.get('date_of_birth')
        phone_number = request.POST.get('phone_number')
        location = request.POST.get('location')
        company_name = request.POST.get('company_name')
        email = request.POST.get('email')
        university = request.POST.get('university')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        print(f"password: {password} --- confirm password: {confirm_password}")

        if password != confirm_password:
            return render(request, 'employees-signup-1.html', {'error': 'Passwords do not match.'})

        employee = Employee(
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            phone_number=phone_number,
            current_location=location,
            company_name=company_name,
            email=email,
            university=university,
        )
        employee.set_password(password)  # This will hash the password correctly
        employee.save()

        return render(request, 'employee-signup-summary.html', {
            'first_name': first_name,
            'last_name': last_name,
            'date_of_birth': date_of_birth,
            'phone_number': phone_number,
            'location': location,
            'company_name': company_name,
            'email': email,
            'university': university,
            'password':password,
        })
    else:
        return redirect('employee_login', {'error': "Could not verify login"})

def employee_signup_summary(request):
    # Check that the request is coming from a valid session after form submission
    if request.method == 'GET' and 'first_name' in request.session:
        employeeInfo = {
            'first_name': request.session.get('first_name'),
            'last_name': request.session.get('last_name'),
            'date_of_birth': request.session.get('date_of_birth'),
            'phone_number': request.session.get('phone_number'),
            'location': request.session.get('location'),
            'company_name': request.session.get('company_name'),
            'email': request.session.get('email'),
            'university': request.session.get('university'),
            'password' : request.session.get('password'),
        }
        return render(request, 'employee-signup-summary.html', employeeInfo)
    else:
        # Redirect to signup form if data is missing or accessed directly
        return redirect('employee_signup')
    
def employee_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Use Django's built-in authenticate function
        user = authenticate(request, email=email, password=password)
        print(f"user authentication: {user}")

        if user is not None:
            # Log the user in
            login(request, user)
            return redirect('employee_login_successful')
        else:
            return render(request, 'employees-login.html', {'error': 'Invalid email or password.'})

    return render(request, 'employees-login.html')


def employee_login_successful(request):
    return render(request, 'employee-login-successful.html', {})  