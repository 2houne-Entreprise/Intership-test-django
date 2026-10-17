from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello_fun(req):
    return HttpResponse("Hello From TaskFlow App")


