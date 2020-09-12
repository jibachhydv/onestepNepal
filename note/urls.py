from django.urls import path

from . import views

urlpatterns = [
    path('', views.notelist,name='notelist'),
    path('<int:pk>-<slug:slug>/',views.notedetail, name='notedetail'),
    path('new/', views.createNote , name='newnote'),
    path('update/<int:pk>-<slug:slug>/', views.NoteUpdateView.as_view(), name='noteupdate'),
    path('delete/<int:pk>-<slug:slug>/', views.noteDelete, name='notedelete'),
]