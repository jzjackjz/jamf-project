from django.http import HttpResponse
from django.shortcuts import render
import requests
import json

def home_view(request, *args, **kwargs):
    response = requests.get("https://mcxlmpfy3k.execute-api.us-east-1.amazonaws.com/dev/animals").json()
    response2 = json.dumps(response)
    animal_list = json.loads(response2)
    my_context = {
        "my_list": animal_list["animals"]
    }
    return render(request,'home.html', my_context)

def dog_view(request, *args, **kwargs):
    return render(request,'dogs.html',{})  

def lion_view(request, *args, **kwargs):
    return render(request,'lions.html',{})  

def horse_view(request, *args, **kwargs):
    return render(request,'horses.html',{})  