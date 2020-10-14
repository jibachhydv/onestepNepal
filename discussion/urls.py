from django.urls import path
from . import views

# app_name = 'discussion'
urlpatterns = [
    path('questions/', views.questionlist, name='allquestions'),
    path('question/<int:id>-<slug:slug>/', views.questiondetail, name='questiondetail'),

    path('ask-question/', views.askquestion, name='askquestion'),


    # Update Question
    path('update/<int:id>-<slug:slug>/', views.QuestionUpdateView.as_view(), name='updatequestion'),

    # Delete Question
    path('deletequestion/<int:id>/', views.deletequestion, name='deletequestion'),

    # Add Answer
    path('addanswer/<int:questionid>/', views.newanswer, name='newanswer'),

    # Delete Answer
    path('deleteanswer/<int:answerid>/', views.deleteanswer, name='deleteanswer'),

    # Search Result By Subject
    path('subject/<str:subject>/', views.searchSubject, name='searchSubjectDiscussion'),

    # Search Result By Grade
    path('grade/<str:grade>/', views.searchGrade, name='searchGradeDiscussion'),
     
]
