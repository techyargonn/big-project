
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('artists/', views.artists, name="artists"),
    path('contact/', views.contact, name="contact"),
]
