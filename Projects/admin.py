from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Sample)
class SampleAdmin(admin.ModelAdmin):
    list_display = ('name','summary','category')        
    ordering = ('name',)
    search_fields = ('name', 'category')

#admin.site.register(Project) # Just to display model in Admin Panel
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title','summary','category')        
    ordering = ('title',)
    search_fields = ('title',)
