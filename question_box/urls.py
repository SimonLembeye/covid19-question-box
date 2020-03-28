from django.urls import path
from . import views

urlpatterns = [
    path('api/question-answer-pair/', views.QuestionAnswerPairList.as_view()),
]