from django.shortcuts import render
from formsapp import forms,models
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    d={
        'form':forms.Exampleform
    }
    return  render(request,'formsapp/index.html',d)
def student(request):
    student=models.Student.objects.all()
    d={
        'student':student
    }
    return render(request,'formsapp/student.html',d)
def addstudent(request):
    if(request.method=='GET'):
        studentform=forms.Studentform()
    if(request.method=='POST'):
        studentform=forms.Studentform(request.POST)
        if(studentform.is_valid()):
            student=studentform.save()
            return HttpResponseRedirect('/students')
    d={
        'studentform':studentform
    }
    return render(request,'formsapp/addstudent.html',d)