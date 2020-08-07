from django.urls import path
from myapp import views
urlpatterns = [
    path('1/',views.index),
    path('2/',views.hello),
]