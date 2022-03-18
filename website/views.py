from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index_view(request):
    return HttpResponse('<h1 style="text-align:center;background:red;"><a href="#">Hello There!!! Welcome To My HomePage!</a></h1>')
def about_view(request):
    return HttpResponse('<h1 style="text-align:center;background:green;"><a href="#">Hello There!!! Welcome To My AboutPage!</a></h1>')
def contact_view(request):
    return HttpResponse('<h1 style="text-align:center;background:grey;"><a href="#">Hello There!!! Welcome To My ContactPage!</a></h1>')