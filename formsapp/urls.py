from django.urls import path
from formsapp import views
urlpatterns=[
    path('index',views.index),
    path('students',views.student),
    path('addstudent',views.addstudent),
]