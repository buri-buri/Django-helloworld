from django import forms

class Example(forms.Form):
    name=forms.CharField()
    about_me=forms.CharField(widget=forms.Textarea())
    active=forms.BooleanField()