from django.http import HttpResponse
from django.shortcuts import render

def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request, "home.html", {})

def animal_view(request, *args, **kwargs):
    return HttpResponse("<h1>Animals</h1>")
