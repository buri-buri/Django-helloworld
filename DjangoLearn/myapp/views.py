from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    developer='sagar kaushik'
    family=['sagar','shivam','varsha','vinita']
    d={'developer':developer,'family':family}
    response=render(request,'myapp\index.html',d)
    return response