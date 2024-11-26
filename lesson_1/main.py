from questions import get_random_question
from student import load_students, get_random_student, update_student


def start_testing():
    """Начинает тестирование студентов."""
    students = load_students()
    if not students:
        print("Список студентов пуст. Добавьте их сначала!")
        return

    while students:
        student = get_random_student()
        print(f"Студент: {student}")

        question = get_random_question()
        if not question:
            print("Вопросы закончились!")
            break

        print(f"Вопрос для {student}: {question}")
        answer = input("Ответ правильный? (да/нет): ").strip().lower()

        if answer == 'нет':
            print(f"{student} удалён из списка.")
            update_student(student, correct=False)
        elif answer == 'да':
            print(f"{student} ответил правильно!")
            update_student(student, correct=True)

        # Обновляем список студентов
        students = load_students()

    print("Тестирование завершено!")


start_testing()