from django.urls import path
from authenticationapp import views
urlpatterns = [
    path('auth',views.auth),
    path('index',views.index),
    path('login',views.login),
    path('log-in',views.Login.as_view()),
    path('log-out',views.Logout.as_view()),
]