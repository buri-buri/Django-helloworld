from django import forms
from formsapp import models
class Exampleform(forms.Form):
    name=forms.CharField()
    about_me=forms.CharField(widget=forms.Textarea())
    active=forms.BooleanField()
class Studentform(forms.ModelForm):
    class Meta:
        model=models.Student
        fields='__all__'
    