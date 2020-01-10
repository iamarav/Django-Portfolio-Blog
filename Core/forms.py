from django import forms

class ContactForm(forms.Form):
  name = forms.CharField(label='Your Name', max_length=100)
  email = forms.EmailField(label='Your Email', max_length=250)
  subject = forms.CharField(label='Subject', max_length=500)
  #  message = forms.CharField(max_length=700)
  message = forms.CharField( widget=forms.Textarea )
  #  ip = request.META['REMOTE_ADDR']

class FeedbackForm(forms.Form):
  name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter your name here'}))
  email = forms.EmailField(label='Email', max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Enter your email here'}))
  phone = forms.CharField(label='Phone', required=False, widget=forms.TextInput(attrs={'placeholder': 'Enter phone number here'}))
  # city_choices = (
  #                 ('DEL', ("Delhi")),
  #                 ('MOH', ("Mohali")),
  #                 ('MUM', ("Mumbai")),
  #                 ('BAN', ("Bangalore")),
  #               )
  # city = forms.ChoiceField(label='Your City', choices=city_choices, initial='MOH', required=True)
  feedback = forms.CharField( widget=forms.Textarea )


class LoginForm (forms.Form):
  username = forms.CharField(label='Username', max_length=100)
  password = forms.CharField(label='Your Password', max_length=50)

class ModProjectForm (forms.Form):
  title = forms.CharField(label='Project Title', max_length=200)
  summary = forms.CharField( label='Project Summary', widget=forms.Textarea )
  category = forms.CharField( label='Category', max_length=200)
  image = forms.ImageField( label='Project Image' )
  link = forms.URLField( label='Project URL' )
