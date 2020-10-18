from django.urls import path

from . import views

urlpatterns = [

    # Read Nepal
    path('', views.readNepal, name='readnepal'),
    path('test/', views.testHomePage, name='testPage'),
    path('bootcamp/', views.testHomePage, name='bootcamp'),
]