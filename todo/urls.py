from django.contrib import admin
from django.urls import path
from LIST.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todo),
]
