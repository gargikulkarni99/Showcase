from django.shortcuts import render, redirect, get_object_or_404
from ..models import Employee, University, Mentor
from django.contrib.auth import authenticate, login

def mentor_signup(request) :
    return render(request,'mentor-signup.html', {})

def mentor_signup_form(request):
    if request.method == 'POST':

        email = request.POST.get('email')

        # Process data or save to session if needed
        request.session['email'] = email

        # Render the next page with the data
        return render(request, 'mentor-signup-1.html', {'email': email})
    else:
        # Redirect or handle non-POST requests
        return redirect('mentor_signup')

def mentor_signup_form_submission(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        date_of_birth = request.POST.get('date_of_birth')
        phone_number = request.POST.get('phone_number')
        location = request.POST.get('location')
        organization_name = request.POST.get('organization_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        print(f"password: {password} --- confirm password: {confirm_password}")

        if password != confirm_password:
            return render(request, 'mentor-signup-1.html', {'error': 'Passwords do not match.'})

        employee = Mentor(
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            phone_number=phone_number,
            current_location=location,
            organization_name=organization_name,
            email=email,
        )
        employee.set_password(password)  # This will hash the password correctly
        employee.save()

        return render(request, 'employee-signup-summary.html', {
            'first_name': first_name,
            'last_name': last_name,
            'date_of_birth': date_of_birth,
            'phone_number': phone_number,
            'location': location,
            'organization_name': organization_name,
            'email': email,
            'password': password,
        })
    else:
        return redirect('mentor-signup-1.html', {'error': "Could not verify login"})
    
def mentor_login(request):
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

    return render(request, 'mentors-login.html')

def mentor_forgotPassword(request):
    return render(request, 'forgot-password-mentors.html')

def mentor_resetPassword(request):
    if request.method == 'POST':

        email = request.POST.get('email')
        # Process data or save to session if needed
        request.session['email'] = email
        # Render the next page with the data
        return render(request, 'forgot-password-mentors-1.html', {'email': email})
    else:
        # Redirect or handle non-POST requests
        return redirect(request, 'forgot-password-mentors-1.html',{'error': 'Invalid email or password.'})
    
def mentor_resetPassword_Submission(request):
    if request.method == 'POST':
        email = request.session.get('email')  # or request.POST.get('email') if not using session
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        # Validate that passwords match
        if new_password != confirm_password:
            return render(request, 'forgot-password-mentors-1.html', {'error': 'Passwords do not match.'})

        try:
            # Retrieve the Mentor by email
            mentor = get_object_or_404(Mentor, email=email)

            # Set the new password (this will automatically hash it)
            mentor.set_password(new_password)
            mentor.save()

            # Redirect to a success page or login page after password reset
            return redirect('home')

        except Mentor.DoesNotExist:
            return render(request, 'forgot-password-mentors-1.html', {'error': 'Employee not found. Please try again.'})

    # Handle GET request or other methods
    return redirect('mentor_forgot_password')