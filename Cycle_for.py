# for i in range(0, 11, 2):
#     print(f"Ваши значения - {i}")
#     for j in range(0, 11, 2):
#         print(f"Ваши вложенные значения: - {j}")
#
# print(None)
#
# for k in range(12, 0, - 2):
#     print(f"Ваши значения - {k}")
#     for l in range(12, 0, - 2):
#         print(f"Ваши вложенные значения: - {l}")

# word = "Python"
#
# for i in word:
#     print(i, end=" ")

# Задача №035.
# you_name = input("Введите своё имя: ")
#
# for i in range(0, 3):
#     print(you_name)

# Задача №036.
# you_name = input("Введите своё имя: ")
# digits = int(input("Введите число: "))
#
# for i in range(0, digits):
#     print(you_name)

# Задача №037.
# you_name = input("Введите своё имя: ")
#
# for i in you_name:
#     print(i)

# Задача №038.
# you_name = input("Введите своё имя: ")
# digits = int(input("Введите число: "))
#
# for i in range(0, digits):
#     for j in you_name:
#         print(j)

# Задача №039.
# number = int(input("Введите число от 1 до 12: "))
#
# for i in range(1, 13):
#     j = i * number
#     print(f"{i} x {number} = {j}")

# Задача №040.
# number_7 = int(input("Введите любое число до 50 включая и само число 50 тоже можно: "))
#
# for i in range(50, number_7 - 1, -1):
#     print(i)

# Задача №041.
# name_1 = str(input("Как ваше имя: "))
# digits_1 = int(input("Введите число: "))
#
# if digits_1 < 10:
#     for i in range(0, digits_1):
#         print(name_1)
# else:
#     print("Too high")

# Задача №042.
# digits_001 = int(input("Введите пять чисел: "))
# question_1 = str(input(f"Хотите ли включить данное число {digits_001} в суммирование? Да, нет? " )).lower()
#
# digits_002 = int(input("Осталось ввести 4 числа: "))
# question_2 = str(input(f"Хотите ли включить данное число {digits_002} в суммирование? Да, нет? " )).lower()
#
# digits_003 = int(input("Осталось ввести 3 числа: "))
# question_3 = str(input(f"Хотите ли включить данное число {digits_003} в суммирование? Да, нет? " )).lower()
#
# digits_004 = int(input("Осталось ввести 2 числа: "))
# question_4 = str(input(f"Хотите ли включить данное число {digits_004} в суммирование? Да, нет? " )).lower()
#
# digits_005 = int(input("Осталось ввести последнее число: "))
# question_5 = str(input(f"Хотите ли включить данное число {digits_005} в суммирование? Да, нет? " )).lower()
#
# answer_1 = question_1
# answer_2 = question_2
# answer_3 = question_3
# answer_4 = question_4
# answer_5 = question_5

print("Вам нужно будет ввести 5 чисел!")

total = 0

for i in range(0, 5):
    num = int(input("Введите число: "))
    question = input(f"Хотите ли включить данное число {num} в суммирование? (да/нет)? ").lower()
    if question == "да":
        total = total + num
print(total)