from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<b>Hello World</b>")

def get_post(request, id):
    return HttpResponse("Hello {}".format(id))

def greet(request, name):
    return HttpResponse("Hello {}".format(name))