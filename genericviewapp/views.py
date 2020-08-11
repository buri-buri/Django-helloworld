from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from genericviewapp import models
from django.views.generic import (
    DetailView,ListView,CreateView,UpdateView,DeleteView)
# Create your views here.
class Index(View):
    def get(self,request):
        return HttpResponse('GET request')
    def post(self,request):
        return HttpResponse('POST request')

class Collegedetail(DetailView):
    model=models.College
    template_name='genericviewapp\collegedetail.html'

class Collegecreate(CreateView):
    model=models.College
    template_name='genericviewapp/collegecreate.html'
    fields='__all__'
    success_url='collegelist'
class Studentcreate(CreateView):
    model=models.Student
    template_name='genericviewapp/studentcreate.html'
    fields='__all__'
    success_url='studentlist'

class Collegeupdate(UpdateView):
    model=models.College
    template_name='genericviewapp/collegecreate.html'
    fields='__all__'
    success_url='/genericviewapp/collegelist'
class Studentupdate(UpdateView):
    model=models.Student
    template_name='genericviewapp/studentcreate.html'
    fields='__all__'
    success_url='/genericviewapp/studentlist'

class Collegelist(ListView):
    model=models.College
    template_name='genericviewapp/collegelist.html'
    context_object_name='colleges'
class Studentlist(ListView):
    model=models.Student
    template_name='genericviewapp/studentlist.html'
    context_object_name='students'

class Collegedelete(DeleteView):
    model=models.College
    template_name='genericviewapp/collegedelete.html'
    success_url='/genericviewapp/collegelist'
class Studentdelete(DeleteView):
    model=models.Student
    template_name='genericviewapp/studentdelete.html'
    success_url='/genericviewapp/studentlist'