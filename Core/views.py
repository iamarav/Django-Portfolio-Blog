from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings

from .forms import *
from .models import *

from Projects.models import Project

from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

# Define Global variables here
media_url = settings.MEDIA_URL
static = settings.STATIC_URL
site_info = settings.SITE_INFO

def HomePage(request):
    passing_dictionary = {                   
                    'static_url' : static,
                    'media_url' : media_url,
                    'site_info': site_info,
                        }
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            the_name = form.cleaned_data['name']
            the_email = form.cleaned_data['email']
            the_feedback = form.cleaned_data['feedback']
            the_phone = form.cleaned_data['phone']
          #  the_city = form.cleaned_data['city']
            form_data = Feedback(name = the_name, email = the_email, phone_number = the_phone, message = the_feedback)
            form_data.save()
            return HttpResponse('Hi, '+str(the_name)+"! Your feedback is received. You will receive a confirmation email on "+str(the_email)+".<br>Thank you!")
        else:
            return HttpResponse('Not a Valid Form')
    feedbackForm = FeedbackForm() 
    passing_dictionary['feedbackForm'] = feedbackForm
    passing_dictionary['projects'] = Project.objects.all()[:3]
    return render( request, 'template-home.html', passing_dictionary)
    
def About(request):
    passing_dictionary = {                   
                    'static_url' : static,
                    'media_url' : media_url,
                    'site_info': site_info,
                        }
    return render( request, 'template-about.html', passing_dictionary)  
    # this renders the html page from template folder to frontent

def ContactPage(request):
    passing_dictionary = {                   
                    'static_url' : static,
                    'media_url' : media_url,
                    'site_info': site_info,
                        }
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            form_data = Contact(name = name, email = email, subject = subject, message = message)
            form_data.save()
            return HttpResponse('Form is submitted!')
        else:
            return HttpResponse('Please check your input and try again!')

    return render( request, 'template-contact.html', passing_dictionary)
    # this renders the html page from template folder to frontent

def LoginPage(request):
    passing_dictionary = {
        'media_url': media_url,
        'site_info': site_info,
        'static_url': static,
    } 
    if 'successLogout' in request.session:
        passing_dictionary ['successLogout'] = 'You are logged out successfully!'
        del request.session['successLogout']
        request.session.modified = True
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username is not "" and password is not "":
            # check credentials
            if '@' in username:
                # user is logging with email
                try:
                    user = User.objects.get(email = username)
                    if user.check_password(password):
                        # Password is correct and user is authenticated
                        print('Password is OK')
                    else:
                        user = None
                        # Password is wrong
                except User.DoesNotExist :
                    #User does not exist with the corresponding email
                    user = None
            else:
                # User is logging with username
                user = authenticate(username= username, password= password)
            if user is not None:
                # Login is success
                auth.login(request, user)
                passing_dictionary ['success'] = 'Woohoo! You are logged in to awesomeness.'
                return HttpResponseRedirect('/dashboard') 
                # return render( request, 'core/template-dashboard.html', passing_dictionary )
            else:
                # There is some error while logging in 
                passing_dictionary ['errors'] = 'Invalid Credentials buddy! Try again.' 
                return render( request, 'accounts/template-login.html', passing_dictionary )
        else:
            # Throw error of empty password
            passing_dictionary ['errors'] = 'Enter valid values.' 
            return render( request, 'accounts/template-login.html', passing_dictionary )
    else:
        return render( request, 'accounts/template-login.html', passing_dictionary )
        # to show the login page if there is no Form POSTED

def SignupPage(request):
    passing_dictionary = {
        'media_url': media_url,
        'static_url': static,
        'site_info': site_info,
    }
    if request.method == 'POST':
        email = request.POST.get('username')
        if '@' not in email:
            # User has entered invalid email. We can also use regex here.
            passing_dictionary ['errors'] = 'Enter a valid email.' 
            return render( request, 'accounts/template-signup.html', passing_dictionary)
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        if password1 == password2:
            try:
                # Checking if the email entered is already existing in our DB.
                user = User.objects.get(email = email)
                passing_dictionary ['errors'] = 'Email already exists.' 
                return render( request, 'accounts/template-signup.html', passing_dictionary)
            except User.DoesNotExist :
                # The user does not exist.
                username = email.split('@', 1)[0] # just to remove the rest of the part after email
                try:
                    usernameExists = User.objects.get(username = username) # just to check if the username exists
                    username += str(1) # appending some additional text at the end
                except User.DoesNotExist :
                    username = username # No Change
                user = User.objects.create_user(email=email, username = username, first_name = fname, last_name = lname, password=password1)
#                auth.login(request,user) # This can be used to automatically login after successful signup.
                # Sign Up Success
                passing_dictionary ['success'] = 'Signup Success. Login to continue.' # Sending Signup Success Message.
                return render( request, 'accounts/template-login.html', passing_dictionary )
        else:
            # The Passwords entered are not identical.
            passing_dictionary ['errors'] = 'Passwords must match.' 
            return render( request, 'accounts/template-signup.html', passing_dictionary )
    else:
        # No POST request received.
        return render( request, 'accounts/template-signup.html', passing_dictionary )
        #to make a signup page

# DASHBOARD CONTENT AHEAD

@login_required(login_url='/user/login/')
def DashboardPage(request):
    passing_dictionary = {
        'media_url': media_url,
        'static_url': static,
        'site_info': site_info,
    }
    return render( request, 'core/template-dashboard.html', passing_dictionary )

@login_required(login_url='/')
def Logout(request):
    auth.logout(request) #logout the current user
    request.session['successLogout'] = 'You are now logged out successfully!' #logout message
    return HttpResponseRedirect('/user/login')


def AddBlogPostPage(request):
    passing_dictionary = {
        'media_url': media_url,
        'static_url': static,
        'site_info': site_info,
    }
    return render( request, 'core/template-dashboard.html', passing_dictionary )