import random

# Возможные варианты
choices = ["камень", "ножницы", "бумага"]

# Ввод пользователя
user_choice = input("Выберите (камень, ножницы, бумага): ").lower()

# Случайный выбор компьютера
computer_choice = random.choice(choices)
print(f"Компьютер выбрал: {computer_choice}")

# Определение победителя
if user_choice == computer_choice:
    print("Ничья!")
elif (user_choice == "камень" and computer_choice == "ножницы") or \
     (user_choice == "ножницы" and computer_choice == "бумага") or \
     (user_choice == "бумага" and computer_choice == "камень"):
    print("Вы победили! 🎉")
else:
    print("Вы проиграли. 😔")