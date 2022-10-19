# Task 1. Задайте список из нескольких чисел. Напишите программу,
#  которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# count = int(input('Количество чисел в списке = '))
# some_list = []
# for i in range(count):
#     number = int(input('Вводите числа по одному - '))
#     some_list.append(number)
# sum =0
# for number in range(1, count, 2):
#     sum += some_list[number]
# print(f'Сумма = {sum}')


# Task 2.Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# count = int(input('Количество чисел в списке = '))
# some_list = []
# for i in range(count):
#     number = int(input('Вводите числа по одному - '))
#     some_list.append(number)
# product_list = []
# for i in range((count - 1) //2 + 1):
#     prod = some_list[i] * some_list[count- i - 1]
#     product_list.append(prod)
# print(product_list)


# Task 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
#  между максимальным и минимальным значением дробной части элементов.

# count = int(input('Количество чисел в списке = '))
# some_list = []
# for i in range(count):
#     number = input('Вводите числа по одному - ')
#     some_list.append(number)
# fraction_list = []
# for i in some_list:
#     if '.' in str(i):
#         fraction = str(i).split('.')[1]
#         fraction_list.append(fraction)
# maxx = max(fraction_list)
# minn = min(fraction_list)
# print(float('0.' + maxx) -float('0.' + minn))


# Task 4.Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# decimall = int(input('Введите число - '))
# binaryy = ''
# while decimall != 0:
#     binaryy = str(decimall % 2) + binaryy
#     decimall //= 2
# print(binaryy)