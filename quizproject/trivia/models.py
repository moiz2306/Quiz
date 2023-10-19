from django.db import models
from django.db.models import Model

class TriviaQuestion(Model):
    question_id: int = models.PositiveIntegerField(unique=True)  # Уникальный ID вопроса
    question_text: str = models.TextField()  # Текст вопроса
    answer_text: str = models.TextField()  # Текст ответа
    creation_date = models.DateTimeField(auto_now_add=True)  # Дата создания вопроса в нашей базе данных

    def __str__(self) -> str:
        return self.question_text

    class Meta:
        verbose_name = "Вопрос викторины"
        verbose_name_plural = "Вопросы викторины"