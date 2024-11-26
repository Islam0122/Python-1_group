# number = []
# jup_sandar = []
# tak_sandar =[]
# for i in range(1,101):
#     if i%2 == 0:
#         jup_sandar.append(i)
#     if i%2 == 1:
#         tak_sandar.append(i)
#     number.append(i)
#
# print(number)
# print(jup_sandar)
# print(tak_sandar)

# numbers = list(range(1,101))
# jup_sandar = list(filter(lambda x: x % 2 == 0, numbers))
# tak_sandar = list(filter(lambda x: x % 2 == 1, numbers))
# print(f"{numbers}\n{jup_sandar}\n{tak_sandar}")

print(f"numbers:{list(range(1,101))} \n"
      f" jup_sandar {list(range(2,101,2))} \n"
      f" tak_sandar {list(range(1,101,2))}")

