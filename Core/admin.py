from django.contrib import admin

# Register your models here.

from .models import *

#admin.site.register(Feedback)
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'message')    
    search_fields = ('name','email',)

#admin.site.register(Contact)
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','phone_number','subject','date','time')
