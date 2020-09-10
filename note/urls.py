from django.urls import path

from . import views

urlpatterns = [
    path('', views.NoteList.as_view(), name='notelist'),
    path('<int:pk>/', views.NoteDetail.as_view(), name='notedetail'),
    path('new/', views.NoteCreate.as_view(), name='newnote'),
]