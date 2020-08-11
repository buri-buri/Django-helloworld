from django.contrib import admin
from django.urls import path,include
from myapp import urls
from modelapp import urls
from relationshipapp import urls
from formsapp import urls
from genericviewapp import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/',include('myapp.urls')),
    path('modelapp/',include('modelapp.urls')),
    path('relationshipapp/',include('relationshipapp.urls')),
    path('formsapp/',include('formsapp.urls')),
    path('genericviewapp/',include('genericviewapp.urls')),
]