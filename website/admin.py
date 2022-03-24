from django.contrib import admin
from website.models import Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','created_date')
    list_filter = ('email')
    search_fields = ['']
admin.site.register(Contact)