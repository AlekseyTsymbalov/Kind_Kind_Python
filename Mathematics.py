import math     # Подключил библиотеку математических функций

# num = 12.5678
# print(round(num, 2)) # Вывод 12.58
# print(10 ** 2)
# num2 = 120
# print(math.sqrt(num2))
# print(round(math.sqrt(num2), 2))
#
# print(round(15 / 7, 2))
# print(15 // 7)
# print(15 / 2)
# print(15 % 2)

# Задача №027.  Предложите пользователю ввести число
# с большим количеством знаков в дробной
# части. Умножьте это число на 2 и выведите ответ.
# num_dot = float(input("Введите число с большим количеством знаков, после запятой: "))
# result = num_dot * 2
#
# print(result)

# Задача №028. Измените программу из задачи 027 так, чтобы она
# выводила результат с точностью до двух знаков
# в дробной части.
# num_dot = float(input("Введите число с большим количеством знаков, после запятой: "))
# result = num_dot * 2
#
# print(round(result, 2))

# Задача №029. Предложите пользователю ввести целое число больше 500.
# Вычислите квадратный корень из этого числа и выведите его с точностью
# до двух знаков в дробной части
# num_2 = int(input("Введите целое число больше 500: "))
# sqrt = round(math.sqrt(num_2), 2)
#
# print(sqrt)

# Задача №030. Выведите число «пи» (π) с точностью до 5 знаков.
# print(round(math.pi, 5))

# Задача 031. Предложите пользователю ввести радиус круга (рас
# стояние от центра до внешней границы.) Вычислите
# площадь круга (π * радиус2)
# radius = int(input("Введите радиус круга: "))
# sqrt_circle = math.pi * radius * radius # pi * (radius**2)
#
# print(sqrt_circle)

# Задача №032. Предложите пользователю ввести радиус
# и высоту цилиндра. Вычислите его объем (площадь круга * высота)
# и выведите его с точностью до трех знаков.
# sqrt_cylinder = float(input("Введите радиус цилиндра: "))
# cylinder_height = float(input("Введите высоту цилиндра: "))
# area = math.pi * (sqrt_cylinder**2)
# volume = area * cylinder_height
#
# print(round(volume, 3))

# Задача №033. Предложите пользователю ввести два числа. Используйте целочисленное деление,
# чтобы разделить первое число на второе; вычислите остаток и выведите
# ответ в виде, удобном для пользователя (например, если пользователь ввел 7 и 2,
# выведите строку вида «если разделить 7 на 2, получится 3 с остатком 1»).
# num_3 = int(input("Введите первое число: "))
# num_4 = int(input("Введите второе число: "))
# summ = num_3 // num_4
# summ2 = num_3 % num_4
#
# print(f"Если разделить {num_3} на {num_4}, получится {summ} с остатком {summ2}")

# Задача №034. Выведите следующее сообщение:
#  1) Square
#  2) Triangle
#  Enter a number:
#  Если пользователь вводит 1, программа запрашивает длину стороны квадрата и выводит его площадь.
#  Если пользователь вводит 2, программа запрашивает длину стороны и высоту треугольника, проведенную
#  к этой стороне, после чего выводит его площадь. Если пользователь вводит что-то другое, программа должна
#  выдать подходящее сообщение об ошибке.
# proposal = input('''1) Square
# 2) Triangle
# Enter a number: ''')
# choice = proposal
#
# if choice == "1":
#     long_square = int(input("Введите длину стороны квадрата: "))
#     sqrt =   long_square * long_square # area = round(math.sqrt(long_square), 2)
#     print(f"Площадь квадрата = {sqrt}")
# elif choice == "2":
#     long_triangle = int(input("Введите длину  стороны треугольника: "))
#     height_triangle = int(input("Введите высоту треугольника: "))
#     sqrt_triangle = long_triangle * height_triangle / 2
#     print(f"Площадь треугольника = {sqrt_triangle}")
# else:
#     print("Вы ввели недопустимые данные!")
# for i in range(2, 6  + 1):
#     print(i)


# print(13 // 2)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for digits in numbers:
    is_prime = True

    if digits < 2:
        is_prime = False
        continue

    for  divider in range(2, (digits // 2) + 1): # range(2, (digits // 2) + 1):
        if digits % divider == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(digits)
    else:
        not_primes.append(digits)

print(f"Исходный код:\nnumbers = {numbers}")
print(f"Primes: {primes}")
print(f"Not Primes: {not_primes}")