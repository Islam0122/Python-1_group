import random

from colorama import Fore, Style, init

money = 500


def start_game():
        print(f"{Fore.BLUE}welcome to game \n {Fore.GREEN}money : ", money, end="$\n")

        bot_choices_number = random.randint(1, 100)
        attempts = 0

        while True:
            if money < 5:
                print(f"{Fore.RED}акчан жетпейт{Style.BRIGHT}")
                break
            try:
                guess = int(input(f"{Fore.MAGENTA}Введите ваше число (от 1 до 100): "))
                attempts += 1
                if guess < 1 or guess > 100:
                    print("Пожалуйста, введите число в диапазоне от 1 до 100.")
                    continue
                elif guess < bot_choices_number:
                    print("Загаданное число больше.")

                elif guess > bot_choices_number:
                    print("Загаданное число меньше.")

                else:
                    print(f"Поздравляем! Вы угадали число {bot_choices_number} за {attempts} попыток.")
                    break

            except ValueError:
                print(f"{Fore.RED}error")




def watch_my_money():
    print(f"{Fore.YELLOW}Your money is", money , end="$")


print("welcome boss")
text = input("What do you want? 1/2: ")
if text == "1":
    watch_my_money()
elif text == "2":
    start_game()
else:
    text = input(" Error / What do you want? 1/2")
