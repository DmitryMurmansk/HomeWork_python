# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11 "


# def InputNumbers(inputText):
#     is_OK = False
#     while not is_OK:
#         try:
#             number = float(input(f"{inputText}"))
#             is_OK = True
#         except ValueError:
#             print("Это не число!")
#     return number


# def sumNums(num):
#     sum = 0
#     for i in str(num):
#         if i != ".":
#             sum += int(i)
#     return sum


# num = InputNumbers("Введите число: ")

# print(f"Сумма цифр = {sumNums(num)}")

# ___________________________________________

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:  - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4) 

# num = int(input('Введите число: '))
# def factorial(num):
#     if num == 1:
#         return 1
#     else:
#         return factorial(num-1)
# print(factorial(num))
# _________________________________________________

# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

# n = int(input('Введите число n: ')) 
# if n > 0:
#     list = {}
#     sum = 0
#     for x in range(1, n+1):
#         list[x] = round((1+1/x)**x, 2)
#         sum += float(list[x])
#         print(f'Список из чисел: {list}')
#         print(f'Сумма элементов: {round(sum, 2)}')

# ___________________________________________________
# Реализуйте алгоритм перемешивания списка.

# import random

# list = [2,3,4,5,78,9]

# list_shuffled = []
# for x in range(0, len(list)):
#     z = random.randrange(0, len(list))
#     list_shuffled.append(list(z))
#     list.remove(list(z))
# print(list_shuffled)