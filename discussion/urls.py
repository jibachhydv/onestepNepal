from django.urls import path
from . import views


urlpatterns = [
    path('questions/', views.questionlist, name='allquestions'),
    path('question/<int:id>-<slug:slug>/', views.questiondetail, name='questiondetail'),

    path('ask-question/', views.askquestion, name='askquestion'),


    # Update Question
    path('update/<int:id>-<slug:slug>/', views.QuestionUpdateView.as_view(), name='updatequestion'),

    # Delete Question

]
