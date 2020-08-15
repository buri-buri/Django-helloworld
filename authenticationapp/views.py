from django.shortcuts import render
from authenticationapp import models,forms
from django.contrib.auth import authenticate,login as auth_login
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView,LogoutView
# Create your views here.
class Login(LoginView):
    template_name='authenticationapp/login.html'
    redirect_authenticated_user=True
class Logout(LogoutView):
    pass
def auth(request):
    return HttpResponse('This is valid DEER (Selmon Bhai)')
def index(request):
    return render(request,'authenticationapp/index.html')
def login(request):
    error=None
    loginform=forms.LoginForm()
    if(request.method=="POST"):
        loginform=forms.LoginForm(request.POST)
        if(loginform.is_valid()):
            username=loginform.cleaned_data['username']
            password=loginform.cleaned_data['password']
            user=authenticate(username=username,password=password)
            if(user):
                auth_login(request,user)
                print('user is -',user)
                return HttpResponseRedirect('/authentication/auth')
            else:
                error='Invalid Username or Password'

    d={
        'form':loginform,
        'error':error,
    }
    return render(request,'authenticationapp/login.html',d)