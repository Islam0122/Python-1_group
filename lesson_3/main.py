from colorama import Fore, Style, init


def analyze_string(s):
    letters = sum(1 for char in s if char.isalpha())
    digits = sum(1 for char in s if char.isdigit())
    total = len(s)

    percent_letters = (letters / total) * 100 if total > 0 else 0
    percent_digits = (digits / total) * 100 if total > 0 else 0

    print(f"{Fore.CYAN}Количество букв: {Fore.GREEN}{letters}")
    print(f"{Fore.CYAN}Количество цифр: {Fore.GREEN}{digits}")
    print(f"{Fore.CYAN}Процент букв: {Fore.YELLOW}{percent_letters:.2f}%")
    print(f"{Fore.CYAN}Процент цифр: {Fore.YELLOW}{percent_digits:.2f}%")


user_input = input(f"{Fore.MAGENTA}Введите строку: {Style.BRIGHT}")
analyze_string(user_input)
