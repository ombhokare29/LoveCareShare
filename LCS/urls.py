from django.contrib import admin
from django.urls import path
from LCS import views

urlpatterns = [
    
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("joinus", views.joinus, name='joinus'),
    path("contact", views.contact, name='contact'),
    path("donate", views.donate, name='donate'),
    
]
