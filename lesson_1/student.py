#
import random

def add_student():
    students = input("Введите новых студентов через запятую: ").split(",")
    with open('student_list.txt', 'a') as file:
        for student in students:
            file.write(student + "\n")
            # print(student)

def load_students():
    """Загружает список студентов из файла student_list.txt."""
    try:
        with open('student_list.txt', 'r') as file:
            my_list = []
            for line in file:
                my_list.append(line.strip())
            return my_list
            # return [line.strip() for line in file]
    except FileNotFoundError:
        return []


def get_random_student():
    """Возвращает случайного студента."""
    students = load_students()
    if students:
        return random.choice(students)
    else:
        return None

    # if not students:
    #     return None
    # else:
    #     return random.choice(students)

    # return random.choice(students) if students else None


print(get_random_student())



# С.Жумакадыр
# А.Азирет
# Т.Элмырза


# with open('student_list.txt','r') as file :
#     for student in file:
#         print(student)
#         # print(student)