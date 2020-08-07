from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    developer='sagar kaushik'
    family=['sagar','shivam','varsha','vinita']
    check=True
    d={'developer':developer,'family':family,'check':check}
    response=render(request,'myapp\index.html',d)
    return response
def hello(request):
    return render(request,'myapp\hello.html')