from atexit import register
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from blog.models import Post,Category
from blog.models import Comment

# Register your models here.



class PostAdmin(SummernoteModelAdmin):
    date_hierarchy='created_date'
    empty_value_display = '-empty-'
    list_display = ('Title','author','counted_view','status','published_date','created_date')
    list_filter = ('status','author',)
    search_fields = ['Title','Content']


class CommentAdmin(admin.ModelAdmin):
    date_hierarchy='created_date'
    empty_value_display = '-empty-'
    list_display = ('name','post','approach','created_date')
    list_filter = ('post','approach',)
    search_fields = ['name','post']


admin.site.register(Comment,CommentAdmin)
admin.site.register(Category)
admin.site.register(Post,PostAdmin)
