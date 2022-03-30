from atexit import register
from django.contrib import admin
from blog.models import Post,Category
# Register your models here.



class PostAdmin(admin.ModelAdmin):
    date_hierarchy='created_date'
    empty_value_display = '-empty-'
    list_display = ('Title','author','counted_view','status','published_date','created_date')
    list_filter = ('status','author',)
    search_fields = ['Title','Content']

admin.site.register(Category)
admin.site.register(Post,PostAdmin)
