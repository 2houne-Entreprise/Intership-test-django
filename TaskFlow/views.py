from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from .forms import RegisterForm

# Create your views here.
def hello_fun(req):
    return HttpResponse("Hello From TaskFlow App")


@login_required
def home_view(req):
    return render(req,"dashboard.html")
    
def register_view(req):
    if req.user.is_authenticated:
        return redirect("dashboard")
        
    if req.method=="POST":
        form = RegisterForm(req.POST)

        if form.is_valid():
            user=form.save()
            login(req,user)
            return redirect("dashboard")
    else:
        form=RegisterForm()
    return render(req,"register.html",{"form":form}) 




def login_view(req):
    if req.user.is_authenticated:
        return redirect("dashboard")
    if req.method=="POST":
        form=AuthenticationForm(req,data=req.POST)

        if form.is_valid():
            user=form.get_user()
            login(req,user)
            return redirect("dashboard")
    else:
        form=AuthenticationForm(req)
        
    return render(req,"login.html",{"form":form})


def  logout_view(req):
    if req.method=="POST":
        logout(req)
        return redirect("login")
    return redirect("dashboard")
    
            
def projetcs_view(req):
    return render(req,"projets/list_view.html")