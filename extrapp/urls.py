from django.urls import path

from . import views

urlpatterns = [

    # Read Nepal
    path('', views.readNepal, name='readnepal'),
]