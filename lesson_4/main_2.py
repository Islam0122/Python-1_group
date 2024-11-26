# Запрашиваем имя у пользователя
name = input("Введите ваше имя: ")

# Запрашиваем день и месяц рождения по отдельности
day = int(input("Введите ваш день рождения (ДД): "))
month = int(input("Введите ваш месяц рождения (ММ): "))

# Определяем знак зодиака
if (month == 1 and day >= 20) or (month == 2 and day <= 18):
    zodiac_sign = "Водолей"
elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
    zodiac_sign = "Рыбы"
elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
    zodiac_sign = "Овен"
elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
    zodiac_sign = "Телец"
elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
    zodiac_sign = "Близнецы"
elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
    zodiac_sign = "Рак"
elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
    zodiac_sign = "Лев"
elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
    zodiac_sign = "Дева"
elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
    zodiac_sign = "Весы"
elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
    zodiac_sign = "Скорпион"
elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
    zodiac_sign = "Стрелец"
else:
    zodiac_sign = "Козерог"

# Выводим результат
print(f"{name}, ваш знак зодиака: {zodiac_sign}")
