# while

# i = 0
# while i < 11:
#     print("number = ",i)
#     i += 1

password = "1234"
counter = 0
entered_password = input("Enter your password: ")
while entered_password != password:
    entered_password = input("Enter your password: ")
    counter += 1
print("welcome  c:", counter)
