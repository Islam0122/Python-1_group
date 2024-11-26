

full_name = input('Enter your full name: ')
print("Welcome "+full_name)
age = input('Enter your age: ')
jobs = input('Enter your jobs: ')


monday = float(input('Enter your monday  -> money :  '))
tuesday = float(input('Enter your tuesday  -> money : '))
wednesday = float(input('Enter your wednesday  -> money : '))
thursday = float(input('Enter your thursday  -> money : '))
friday =  float(input('Enter your friday  -> money : '))
saturday = float(input('Enter your saturday  -> money : '))
sunday = float(input('Enter your sunday  -> money : '))


total_expenses = (monday+tuesday+wednesday+thursday+friday+saturday+sunday)
print('Your total expenses is: ',total_expenses , end='$')
average_expense = total_expenses/7
print(f'Your average expense is: {average_expense:.2f}',end="$")
