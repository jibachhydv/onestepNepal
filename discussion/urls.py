from django.urls import path
from . import views


urlpatterns = [
    path('questions/', views.questionlist, name='allquestions'),
    path('question/<int:id>/', views.questiondetail, name='questiondetail'),
]
