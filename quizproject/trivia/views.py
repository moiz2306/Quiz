
import logging
import requests
from typing import List

from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from .models import TriviaQuestion

# Настроим логирование
logger = logging.getLogger(__name__)


@api_view(['POST'])
def trivia_question(request: Request) -> Response:
    """
    Endpoint для получения вопросов викторины из внешнего API и их сохранения в базе данных.

    Аргументы:
    - questions_num (int): Количество вопросов для получения.

    Возвращает:
    - dict: Последний вопрос викторины, сохраненный в базе данных, или пустой объект, если таковых нет.
    """
    questions_num: int = request.data.get('questions_num', 1)
    new_questions: List[TriviaQuestion] = []

    while len(new_questions) < questions_num:
        try:
            response = requests.get(f"https://jservice.io/api/random?count={questions_num - len(new_questions)}", timeout=10)
            response.raise_for_status()  # Будет вызвано исключение, если HTTP-запрос завершился ошибкой
            questions = response.json()
        except requests.RequestException as e:
            logger.error(f"Ошибка при запросе к внешнему API: {e}")
            return Response({"error": "Проблема с получением вопросов. Попробуйте позже."}, status=500)

        ids = [q['id'] for q in questions]
        existing_questions = TriviaQuestion.objects.in_bulk(ids)

        for question_data in questions:
            question_id = question_data['id']
            if question_id not in existing_questions:
                new_questions.append(TriviaQuestion(
                    question_id=question_data['id'],
                    question_text=question_data['question'],
                    answer_text=question_data['answer'],
                    creation_date=question_data['created_at']
                ))

    if new_questions:
        TriviaQuestion.objects.bulk_create(new_questions)
        logger.info(f"Добавлено {len(new_questions)} новых вопросов.")

    # Если есть сохраненные вопросы, вернуть последний, иначе вернуть пустой объект
    last_question = TriviaQuestion.objects.last()
    if last_question:
        return Response({
            'question': last_question.question_text,
            'answer': last_question.answer_text
        })
    else:
        return Response({})
