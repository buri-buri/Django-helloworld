from django.urls import path
from formsapp import views
urlpatterns=[
    path('index',views.index),
    path('student',views.student),
    path('addstudent',views.addstudent),
]