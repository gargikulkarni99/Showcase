from django.shortcuts import render, redirect

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