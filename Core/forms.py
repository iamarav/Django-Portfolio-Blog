from django import forms

class ContactForm(forms.Form):
  name = forms.CharField(label='Your Name', max_length=100)
  email = forms.EmailField(label='Your Email', max_length=250)
  subject = forms.CharField(label='Subject', max_length=500)
  #  message = forms.CharField(max_length=700)
  message = forms.CharField( widget=forms.Textarea )
  #  ip = request.META['REMOTE_ADDR']

class FeedbackForm(forms.Form):
  name = forms.CharField(label='Your name', max_length=100)
  email = forms.EmailField(label='Your Email', max_length=200)
  phone = forms.CharField(label='Your Phone Number', required=False)
  city_choices = (
                  ('DEL', ("Delhi")),
                  ('MOH', ("Mohali")),
                  ('MUM', ("Mumbai")),
                  ('BAN', ("Bangalore")),
                )
  city = forms.ChoiceField(label='Your City', choices=city_choices, initial='MOH', required=True)
  feedback = forms.CharField( widget=forms.Textarea )


class LoginForm (forms.Form):
  username = forms.CharField(label='Username', max_length=100)
  password = forms.CharField(label='Your Password', max_length=50)
