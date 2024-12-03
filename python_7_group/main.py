# fullname = input('Enter your full name: ')
# age = int(input('Enter your age: '))
# """ input -> str  """
#
# def age_year(age):
#     return 2024 - age
#
#
# print(age_year(age))

number = int(input("Enter a number: "))


def jup_or_tak(n):
    if n % 2 == 0:
        print(f"{n} is  jup san .")
    else:
        print(f"{n} is  tak san .")


jup_or_tak(number)

