from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<b>Hello World</b>")

def random_joke(request):
    # return random_joke
    return HttpResponse("<h1>Random JOke incoming</h1>")

def joke_for(request, sex):
    if sex == "male":
        return HttpResponse("<h1>joke for male</h1>")
    elif sex == "female":
        return HttpResponse("<h1>joke for female</h1>")

def all_jokes(request):
    # return all jokes
    return HttpResponse("<h1>ALL JOKES</h1>")