from django.contrib import admin

# Register your models here.
from .models import *

#admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'excerpt', 'date', 'time',)
    search_fields = ('title',)
    ordering = ('id',)

#admin.site.register(Comment)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','id','post','email','comment','comment_time')        
    search_fields = ('post_id','name','comment',)
    ordering = ('id',)

admin.site.register(Categories)