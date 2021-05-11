"""Kheya URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Home.views import user_input, index, oxygen_view, ambulance_view, food_view, test_view, bed_view, doctor_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_input/', user_input, name='home'),
    path('oxygen/', oxygen_view, name='oxygens'),
    path('ambulance/', ambulance_view, name='ambulances'),
    path('food/', food_view, name='foods'),
    path('bed/', bed_view, name='beds'),
    path('test/', test_view, name='tests'),
    path('doctor/', doctor_view, name='doctors'),
    path('', index, name='index')
]
