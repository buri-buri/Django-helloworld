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
    students=models.Student.objects.all()
    d={
        'students':students
    }
    return render(request,'formsapp/student.html',d)
def addstudent(request):
    if(request.method=='GET'):
        studentform=forms.Studentform()
    if(request.method=='POST'):
        studentform=forms.Studentform(request.POST)
        if(studentform.is_valid()):
            student=studentform.save()
            return HttpResponseRedirect('/formsapp/students')

    d={
        'studentform':studentform
    }
    return render(request,'formsapp/addstudent.html',d)