

while True:
    user_input = input("Ведите  вашу операцию: ")

    if user_input.lower() == "x":
        print(f"вы вышли ")
        break

    try:
        result = eval(user_input)
        print(f"{user_input} = {result}")
    except ValueError:
        print("error")
    except Exception as e:
        print("error ",e)