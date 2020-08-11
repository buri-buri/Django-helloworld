from django.urls import path
from genericviewapp import views
urlpatterns = [
    path('index',views.Index.as_view()),
    path('collegedetail/<int:pk>',views.Collegedetail.as_view(),name='i'),
    path('collegelist',views.Collegelist.as_view()),
    path('studentlist',views.Studentlist.as_view()),
    path('collegecreate',views.Collegecreate.as_view()),
    path('studentcreate',views.Studentcreate.as_view()),
    path('collegeupdate/<int:pk>',views.Collegeupdate.as_view()),
    path('studentupdate/<int:pk>',views.Studentupdate.as_view()),
    path('collegedelete/<int:pk>',views.Collegedelete.as_view()),
    path('studentdelete/<int:pk>',views.Studentdelete.as_view())
]