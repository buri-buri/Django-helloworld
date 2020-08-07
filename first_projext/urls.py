from django.contrib import admin
from django.urls import path,include
from myapp import urls
from modelapp import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/',include('myapp.urls')),
    path('modelapp/',include('modelapp.urls'))
]