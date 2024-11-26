import random


def load_questions():
    """Загружает список вопросов из файла questions.txt."""
    try:
        with open('questions.txt', 'r',encoding='utf-8') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return []


def get_random_question():
    """Возвращает случайный вопрос."""
    questions = load_questions()
    return random.choice(questions) if questions else None