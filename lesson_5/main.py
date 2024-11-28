""" pip install  colorama"""

from colorama import Fore, Style, init

"""int ,float ,complex -> Числовые типы данных"""

# int ->  Это тип данных для целых чисел без десятичной точки
# a = 5
# print(type(a))  # --> <class 'int'>

# float -> Это тип данных для чисел с десятичной точкой.
# x = 5.5
# print(type(x)) # --> <class 'float'>

# complex -> Это тип данных для комплексных чисел, состоящих из действительной и мнимой части.
# z = 4j*5j
# print(type(z)) # --> <class 'complex'>


""" str -> Строки в Python  """
# print(type("hello world")) # --> <class 'str'>
s = " H l l o"
# print(type(s))
# print(s[1:4])
# print(s[:3])
# print(s[2:])

# print("l" in s)
# print(s*3)

# s = "  Привет,  мир!  "
# print(s.strip())    # Результат: "Привет, мир!"
# print(s.lower())    # Результат: "  привет, мир!  "
# print(s.replace("мир", "Python"))  # Результат: "  Привет, Python!  "
# print(s.upper())
# print(s.capitalize())
# print(s.split()) # --> list

# s = "  Привет,\n  мир!  "


""" Булев тип (bool) """

# lamp = True
# if lamp:
#     print("lamp on")
# else:
#     print("lamp off")

# print(bool(1+1 == 2 ))


# a = int(input(" a = : "))
# b = int(input(" b = : "))

# p = (a+b)*2
# s = a*b
# print(f'P = {p}\n'
#       f'S = {s}')

# def check (x,y):
#    x = int(x)
#    y = int(y)
#
#    print(x**y)
#
#
# x = input("enter x : ")
# y = input("enter y : ")
# check(x,y)

# full_name = input("enter your full name: ")
# print(f'{Fore.RED}welcome '+full_name)



