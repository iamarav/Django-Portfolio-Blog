from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.conf import settings
from datetime import datetime, timedelta
from django.utils import timezone


from .forms import *
from .models import *

from Projects.models import Project
from Blog.models import *

from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string


# Define Global variables here
media_url = settings.MEDIA_URL
static = settings.STATIC_URL
site_info = settings.SITE_INFO
LOGIN_URL = settings.LOGIN_URL
LOGOUT_URL = settings.LOGOUT_URL

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
    if request.user.id :
        # send user to dashboard if already logged in 
        return HttpResponseRedirect ('/dashboard')
    if 'successLogout' in request.session:
        # display message of successful logout if exists.
        passing_dictionary ['successLogout'] = 'You are logged out successfully!'
        del request.session['successLogout']
        request.session.modified = True
    if request.method == 'POST':
        # if form is submitted
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
    if request.user.id :
        # send user to dashboard if already logged in 
        return HttpResponseRedirect ('/dashboard')
    if request.method == 'POST':
        # if signup form is submitted
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

def ForgotPassword(request, action=None):
    passing_dictionary = {
        'media_url': media_url,
        'static_url': static,
        'site_info': site_info,
    }
    if action == 'checkemail':
        return render( request, 'accounts/template-forgot-password-check-mail.html', passing_dictionary )
    if action == 'success':
        return render( request, 'accounts/template-forgot-password-reset-success.html', passing_dictionary )
    if action == 'new-password':
        user = None
        if request.method == 'POST':
            username = request.POST.get('username')
            token = request.POST.get('token')
            password1 = request.POST.get('password')
            password2 = request.POST.get('password2')
            if password1 != password2:
                print (password1)
                print (password2)
                # the passwords entered are not same
                passing_dictionary ['errors'] = 'Passwords are not identical.'
            else:
                try:
                    if '@' in username:
                        # Email
                        user = User.objects.get(email = username)
                    else:
                        # username
                        user = User.objects.get(username = username)
                except User.DoesNotExist:
                    user = None
                    passing_dictionary ['errors'] = 'Invalid User'
                if user is not None:
                    # User exists.
                    try:
                        if '@' in username:
                            # Email
                            log = ForgotLog.objects.filter(username = user.email).order_by('-id')[:1][0]
                        else:
                            log = ForgotLog.objects.filter(username = user.username).order_by('-id')[:1][0]
                        # passing_dictionary['errors'] = log.date
                        if log.token != request.POST['token']:
                            passing_dictionary ['errors'] = 'Invalid Token!'
                        else:
                            log_date = log.date 
                            now = timezone.now()

                            if now-timedelta(hours=24) <= log_date <= now+timedelta(hours=24):
                                # the token generation date is in last 24 hours
                                print ('OK!')
                                user.set_password(password1)
                                user.save()
                                log.delete()
                                return HttpResponseRedirect ('/user/login')
                            else:
                                passing_dictionary ['errors'] = 'Invalid Token!'
                                print ('Entering a token which is generated before 24 hours!')
                    except ForgotLog.DoesNotExist:
                        # No token found
                        passing_dictionary['errors'] = 'Invalid Combination! Try again.'
        return render( request, 'accounts/template-forgot-password-create-new.html', passing_dictionary )
                    except ForgotLog.DoesNotExist:
                        # No token found
                        passing_dictionary['errors'] = 'Invalid Combination! Try again.'
        return render( request, 'accounts/template-forgot-password-create-new.html', passing_dictionary )
    
    if request.method == 'POST':
        username = request.POST.get('username')
        if username == '' or username is None:
            return HttpResponseRedirect ( '/user/forgot_password/' )
        token = get_random_string(length=32)
        the_data = ForgotLog (username=username, token=token)
        the_data.save()
        print ("username: "+str(username)+", token: "+str(token))
        return HttpResponseRedirect ( '/user/forgot_password/checkemail' )
    else:
        return render( request, 'accounts/template-forgot-password.html', passing_dictionary )

# DASHBOARD CONTENT AHEAD

@login_required( login_url= LOGIN_URL )
def DashboardPage(request):
    passing_dictionary = {
        'media_url': media_url,
        'static_url': static,
        'site_info': site_info,
    }
    passing_dictionary ['number_blog_posts'] = Post.objects.count()
    passing_dictionary ['number_blog_categories'] = Categories.objects.count()
    passing_dictionary ['number_blog_comments'] = Comment.objects.count()
    passing_dictionary ['number_projects'] = Project.objects.count()
    passing_dictionary ['number_cf_response'] = Project.objects.count()
    passing_dictionary ['number_feedback_response'] = Project.objects.count()

    return render( request, 'core/template-dashboard.html', passing_dictionary )

@login_required( login_url= LOGIN_URL)
def Logout(request):
    auth.logout(request) #logout the current user
    request.session['successLogout'] = 'You are now logged out successfully!' #logout message
    return HttpResponseRedirect( LOGIN_URL )

@login_required( login_url= LOGIN_URL )
def ModBlogPostPage(request, action, id):
    passing_dictionary = {
        'media_url': media_url,
        'static_url': static,
        'site_info': site_info,
    }
    if request.method == 'POST':
        if action == 'edit':
            # Editing the current post with form
            post_title = request.POST.get('title')
            content = request.POST.get('content')
            excerpt = request.POST.get('excerpt')

            category = request.POST.get('category')

            try:
                category_instance = Categories.objects.get(category = category)
            except Categories.DoesNotExist:
                new_category = Categories(category = category)
                new_category.save()
                category_instance = Categories.objects.get(category = category)
            
            post_img = ''
            if request.FILES:
                post_img = request.FILES['featured_image']

            post = Post.objects.get(id = id)
            if post:
                post.title = post_title
                post.content = content
                post.excerpt = excerpt
                post.category = category_instance
                if post_img:
                    post.featured_image = request.FILES['featured_image']
                post.save()

        elif action == 'add':
            # When a new Project is added with dashboard form
            post_title = request.POST.get('title')
            content = request.POST.get('content')
            excerpt = request.POST.get('excerpt')
            category = request.POST.get('category')

            try:
                category_instance = Categories.objects.get(category = category)
            except Categories.DoesNotExist:
                new_category = Categories(category = category)
                new_category.save()
                category_instance = Categories.objects.get(category = category)
            
            post_img = ''
            if request.FILES:
                post_img = request.FILES['featured_image']

            form_data = Post(title = post_title, 
                                content = content, 
                                category = category_instance, 
                                featured_image = post_img,
                                excerpt = excerpt,
                                author_id = request.user.id)
            form_data.save()      
            return HttpResponseRedirect('/dashboard/blog/view/posts/') 
        else:
            raise Http404()

    passing_dictionary ['categories'] = Categories.objects.all()
    
    if action == 'edit':
        passing_dictionary ['action'] = 'edit'
        passing_dictionary ['post_id'] = id
        passing_dictionary ['post'] = Post.objects.filter(id = id)[0]
        return render( request, 'core/template-dashboard-mod-blog-post.html', passing_dictionary )
    elif action == 'add':
        passing_dictionary ['action'] = 'add'
        return render( request, 'core/template-dashboard-mod-blog-post.html', passing_dictionary )
    else:
        raise Http404

@login_required( login_url= LOGIN_URL )
def ViewBlogPostsPage(request):
    passing_dictionary = {
        'media_url': media_url,
        'static_url': static,
        'site_info': site_info,
    }
    if 'successDash' in request.session:
        passing_dictionary ['successDash'] = request.session['successDash']
        del request.session['successDash']
        request.session.modified = True
    passing_dictionary['posts'] = Post.objects.all().order_by('-id')
    return render( request, 'core/template-dashboard-view-blog.html', passing_dictionary )

@login_required( login_url= LOGIN_URL )
def DeleteItem(request, type, id):
    if type == 'post':
        Post.objects.filter(id=id).delete()
        request.session['successDash'] = 'Post ID: ' + str(id) + ' deleted successfully.'   
        return HttpResponseRedirect ('/dashboard/blog/view/posts/')
    elif type == 'comment':
        Comment.objects.filter(id=id).delete()
        request.session['successDash'] = 'Comment ID: ' + str(id) + ' deleted successfully.'   
        return HttpResponseRedirect ('/dashboard/blog/view/comments/')
    elif type == 'project':
        Project.objects.filter(id=id).delete()
        request.session['successDash'] = 'Project ID: ' + str(id) + ' deleted successfully.'   
        return HttpResponseRedirect ('/dashboard/projects/view/')
    elif type == 'contact':
        Contact.objects.filter(id=id).delete()
        request.session['successDash'] = 'Response ID: ' + str(id) + ' deleted successfully.'   
        return HttpResponseRedirect ('/dashboard/contact_form/responses/')
    elif type == 'feedback':
        Feedback.objects.filter(id=id).delete()
        request.session['successDash'] = 'Feedback ID: ' + str(id) + ' deleted successfully.'   
        return HttpResponseRedirect ('/dashboard/feedback/responses/')
    else:
        raise Http404()

@login_required( login_url= LOGIN_URL )
def ViewBlogCommentsPage(request):
    passing_dictionary = {
        'media_url': media_url,
        'static_url': static,
        'site_info': site_info,
    }
    if 'successDash' in request.session:
        passing_dictionary ['successDash'] = request.session['successDash']
        del request.session['successDash']
        request.session.modified = True

    passing_dictionary['comments'] = Comment.objects.all().order_by('-id')
    return render( request, 'core/template-dashboard-view-comments.html', passing_dictionary )

@login_required(login_url= LOGIN_URL )
def ModProjectPage(request, action, id):
    passing_dictionary = {
        'media_url': media_url,
        'static_url': static,
        'site_info': site_info,
    }
#    passing_dictionary ['categories'] = Categories.objects.all()
    if request.method == 'POST':
        if action == 'edit':
            # Editing the current project with form
            project_title = request.POST.get('title')
            content = request.POST.get('content')
            category = request.POST.get('category')
            project_link = request.POST.get('project_link')
            project_img = ''
            if request.FILES:
                project_img = request.FILES['project_img']

            project = Project.objects.get(id = id)
            if project:
                project.title = project_title
                project.summary = content
                project.category = category
                project.link = project_link
                if project_img:
                    project.images = request.FILES['project_img']
                project.save()

        elif action == 'add':
            # When a new Project is added with dashboard form
            project_title = request.POST.get('title')
            content = request.POST.get('content')
            category = request.POST.get('category')
            project_link = request.POST.get('project_link')
            
            project_img = ''
            if request.FILES:
                project_img = request.FILES['project_img']

            form_data = Project(title = project_title, 
                                summary = content, 
                                category = category, 
                                link =project_link, 
                                images = project_img)
            form_data.save()      
            return HttpResponseRedirect('/dashboard/projects/view/') 
        else:
            raise Http404()
        
    if action == 'edit':
        passing_dictionary ['action'] = 'edit'
        passing_dictionary ['project_id'] = id
        passing_dictionary ['project'] = Project.objects.filter(id = id)[0]
        
        return render( request, 'core/template-dashboard-mod-project.html', passing_dictionary )
    elif action == 'add':
        passing_dictionary ['action'] = 'add'
        return render( request, 'core/template-dashboard-mod-project.html', passing_dictionary )
    else:
        raise Http404

@login_required(login_url= LOGIN_URL )
def ViewProjectsPage(request):
    passing_dictionary = {
        'media_url': media_url,
        'static_url': static,
        'site_info': site_info,
    }
    if 'successDash' in request.session:
        passing_dictionary ['successDash'] = request.session['successDash']
        del request.session['successDash']
        request.session.modified = True
    passing_dictionary['projects'] = Project.objects.all().order_by('-id')
    return render( request, 'core/template-dashboard-view-projects.html', passing_dictionary )

@login_required(login_url= LOGIN_URL )
def ViewFeedbackResponsesPage(request):
    passing_dictionary = {
        'media_url': media_url,
        'static_url': static,
        'site_info': site_info,
    }
    if 'successDash' in request.session:
        passing_dictionary ['successDash'] = request.session['successDash']
        del request.session['successDash']
        request.session.modified = True
    passing_dictionary['feedbacks'] = Feedback.objects.all().order_by('-id')
    return render( request, 'core/template-dashboard-view-feedbacks.html', passing_dictionary )

@login_required(login_url= LOGIN_URL )
def ViewContactResponsesPage(request):
    passing_dictionary = {
        'media_url': media_url,
        'static_url': static,
        'site_info': site_info,
    }
    if 'successDash' in request.session:
        passing_dictionary ['successDash'] = request.session['successDash']
        del request.session['successDash']
        request.session.modified = True
    passing_dictionary['responses'] = Contact.objects.all().order_by('-id')
    return render( request, 'core/template-dashboard-view-contact-responses.html', passing_dictionary )