from django.urls import path
from . import views

urlpatterns = [
    path('trivia/', views.trivia_question, name='trivia_question'),
]
