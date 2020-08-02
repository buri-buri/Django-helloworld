from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    developer='sagar kaushik'
    family=['sagar','shivam','varsha','vinita']
    #family=['hot girls','smart girls','coder girls']
    d={'developer':developer,'family':family}
    response=render(request,'index.html',d)
    return response