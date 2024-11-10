# i = 10
# print(i)
#
# i *= 2
# print(i)
#
# i *= 2
# print(i)
#
# my_fruits = ["apple", "banana", "chery"]
#
# print(my_fruits[0])
# print(my_fruits[1])
# print(my_fruits[2])
#
# my_object = {"X": 10, "Y": True, "Z": "abc"}
#
# print(my_object["X"])
# print(my_object["Y"])
# print(my_object["Z"])

# Работа цикла for ... in ... со списком, а именно его перебор и вывод каждого элемента на экран.
# Происходит запись в созданную переменную elem каждого элемента из списка, каждую итерацию.
# my_list = [True, 10, "abc", {}]
#
# for elem in my_list:
#     print(elem)

# Тоже самое но с кортежем.
# video_info = ("1920x1080", True, 27)
#
# for elem in video_info:
#     print(elem)

# Работа со словарём
# my_object = {"X": 10, "Y": True, "Z": "abc"}
#
# for key in my_object:
#     print(key, my_object[key]) # Для вывода не только ключа, но и его значения

# for el in [1, "abc", True]: # Созданную переменную el создавать со своим именем, что бы
#     print(type(el))         # она не перекликалась с переменными из кода вне цикла
#     print(el)

# for key in {"id": 324}:
#     print(key)

# Но что бы вывести словарь со значением ключа, необходимо его переместить в переменную
my_dict = {"id": 324, "God": 100} # Переменную создаём перед входом в цикл

for key1 in my_dict:
    print(key1)
    print(my_dict[key1])