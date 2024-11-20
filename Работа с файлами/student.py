#
# students = input("Введите новых студентов через запятую: ").split(",")
# with open('student_list.txt', 'a') as file:
#     for student in students:
#         file.write(student.strip() + '\n')
# print("Студенты добавлены!")
#
#
# with open('student_list.txt', 'r') as file:
#     students_list = [line.strip() for line in file]
#
# if students_list:
#     print("Список студентов:")
#     for student in students_list:
#         print(f"- {student}")


import random


def load_students():
    """Загружает список студентов из файла student_list.txt."""
    try:
        with open('student_list.txt', 'r') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return []


def get_random_student():
    """Возвращает случайного студента."""
    students = load_students()
    return random.choice(students) if students else None


def update_student(student, correct):
    """
    Обновляет статус студента:
    - Удаляет, если ответ неверный.
    - Добавляет звёздочку, если ответ правильный.
    """
    students = load_students()
    if correct:
        students = [f"{s}-*" if s == student else s for s in students]
    else:
        students.remove(student)

    with open('student_list.txt', 'w', encoding='utf-8') as file:
        for s in students:
            file.write(s + '\n')

