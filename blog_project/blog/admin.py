from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display =['title','slug','author','body','publish','created','updated','status']
    list_filter = ('status','created','updated')
    search_fields = ('title','body')
    raw_id_fields = ('author',) #user select on the basis of id
    date_hierarchy = 'publish' #navbar for search old post
    ordering = ['status','publish']
    prepopulated_fields = {'slug':('title',)}
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email' ,'post','created','updated','active')
    list_filter = ('active','created','updated')
    search_fields = ('name','email','body')

admin.site.register(Comment ,CommentAdmin)
admin.site.register(Post , PostAdmin)
