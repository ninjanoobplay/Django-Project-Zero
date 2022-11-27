from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from home.views import index

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('auth/', include('autenticacao.urls')),
    path('home/', include('home.urls')),
]
