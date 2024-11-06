# name = input("Enter you name: ")
# num = int(input("Enter a number: "))
# ID = name + str(num)
# print(ID)

# address = '''Маршала-Воронова 24
# квартира 222
# подъезд 2
# 16 этаж'''
# print(address)

# word = "hello world, and hi people!"
# print(len(word)) # Длина строки в числах
# print(word[7:10]) # Срез начало с и конец по индексу
# print(word.capitalize()) # Выводит Первую букву начала строки с заглавной буквы
# print(word.title()) # Вывод каждое слово в строке с заглавной буквы

# Зада №020
# name = input("Введите своё имя: ")
# print(f"Количество символов в имени: - {len(name)}")

# Зада №021
# name = input("Введите своё имя: ")
# second_name = input("Введите свою фамилию: ")
# full_name = name + " " + second_name
# print(f"{full_name} {len(full_name)}")

# Зада №022
# name = input("Введите своё имя в нижнем регистре: ").title()
# second_name = input("Введите свою фамилию в нижнем регистре: ").title()
# full_name = name + " " + second_name
#
# print(full_name)

# Зада №023
# words = input("Введите строку из стихотворения: ")
# print(len(words))
# print(words[0])
# print(words[-1])

# Зада №024
# name = input("Введите своё имя: ")
# print(name.upper())

# Зада №025
# name = input("Введите своё имя: ")
# if len(name) < 5:
#     second_name = input("Введите свою фамилию: ")
#     full_name = name + second_name
#     print(full_name.upper())
# else:
#     print(name.lower())

# Зада №026
word = str(input("Enter the word: ")).lower()

if word[0] in "aeiou":
    pig_latin = word + "way"
else:
    pig_latin = word[1:] + word[0] +"ay"

print(f"Слово на поросячьей латыни: {pig_latin}")