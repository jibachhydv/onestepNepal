# Importing path module
from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),

    # Login
    path('login/', views.login, name='login'),

    # Logout
    path('logout/', views.logout, name='logout')
]