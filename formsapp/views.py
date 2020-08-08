from django.shortcuts import render
from formsapp import forms
# Create your views here.
def index(request):
    d={
        'form':forms.Example
    }
    return  render(request,'formsapp/index.html',d)