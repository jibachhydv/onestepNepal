from django.urls import path

from . import views

urlpatterns = [
    path('', views.notelist,name='notelist'),
    path('<int:pk>-<slug:slug>/',views.notedetail, name='notedetail'),
    path('new/', views.createNote , name='newnote'),
    path('update/<int:pk>-<slug:slug>/', views.NoteUpdateView.as_view(), name='noteupdate'),
    path('delete/<int:pk>-<slug:slug>/', views.noteDelete, name='notedelete'),

    # New Comment Add
    path('addcomment/<int:noteid>/', views.newcomment, name='newcomment'),

    # Delete Comment
    path('deletecomment-<int:commentid>/', views.deletecomment, name='deletecomment'),

    # Search Result
    path('search/', views.searchAll, name='searchAll'),

    # Search Result By Subject
    path('subject/<str:subject>/', views.searchSubject, name='searchSubject'),

    # Search Result By Grade
    path('grade/<str:grade>/', views.searchGrade, name='searchGrade'),
    
]