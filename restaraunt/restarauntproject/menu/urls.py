from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.foodmenu, name='menu'),
    path('administration/', views.administration, name='administration'),
    path('contact/', views.contact, name='contact'),
]