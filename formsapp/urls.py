from django.urls import path
from formsapp import views
urlpatterns=[
    path('',views.index)
]