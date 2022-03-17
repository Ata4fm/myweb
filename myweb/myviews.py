from django.http import HttpResponse

def myview(request):
    return HttpResponse('<h1 style="text-align:center;background:red;"><a href="#">Hello There!!! Welcome To My Website!</a></h1>')