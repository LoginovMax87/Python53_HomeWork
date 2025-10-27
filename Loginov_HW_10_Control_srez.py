import random
# # 1 Пользователь вводит 4 числа, найти наименьшее из них.

# num1 = int(input("Введите 1-е число: "))
# num2 = int(input("Введите 2-е число: "))
# num3 = int(input("Введите 3-е число: "))
# num4 = int(input("Введите 4-е число: "))
# _min = num1
# if num2<num1: _min=num2
# if num3<_min: _min=num3
# if num4<_min: _min=num4
# print(_min)


#2 Вывести все целые числа кратные 3 в диапазоне от 0 до - 25 (условие в цикле использовать нельзя)!

# for i in range (0, -26, -3):
#     print(i, end=" ")


#3 Пользователь вводит сторону квадрата. Вывести треугольник вписанный в квадрат:

# side = int(input("Введите сторону квадрата: "))
# for i in range(side):
#     for j in range(i):
#         print(" ", end="")
#     for j in range(side-i):
#         print("*", end="")
#     print()


# 4 Пользователь вводит числа до тех пор, пока не введет 0. Подсчитать среднее арифметическое введенных чисел.

# summa = 0
# count = 0
# while True:
#     num = int(input("Введите число: "))
#     if num !=0:
#         summa +=num
#         count += 1
#     else:
#         break
#
# print(summa/count)


# 5 Создать список из 10 элементов, заполнить его случайными числами в заданном пользователем диапазоне

# _list = []
# _min = int(input("Введите начало диапазона: "))
# _max = int(input("Введите конец диапазона: "))
# if _min>_max: _min, _max = _max, _min
# for i in range(10):
#     _list.append(random.randint(_min,_max))
# print(_list)


# # 6 Определить индекс минимального элемента списка

# _min_item = _list[0]
# index_min = 0
# for i in range(1,len(_list)):
#     if _list[i]<_min_item:
#         _min_item = _list[i]
#         index_min = i
# print(index_min+1)

# 7 Напишите функцию, принимающую два одинаковых по размеру списка.
# Первый список проинициализирован, второй пустой.
# Функция должна полностью скопировать элементы первого списка во второй

# list1 = [1,4,2,1,4,64,425,2,1]
# list2 = [0,0,0,0,0,0,0,0,0]
#
# def list_copy(list1,list2):
#     for i in range (len(list1)):
#         list2[i]=list1[i]
#     print(list2)
#
# list_copy(list1,list2)

# 8 Напишите функцию, добавляющую элемент в i-ю позицию списка (возвращает новый список)
# list1 = [1,4,2,1,4,64,425,2,1]
# a = int(input("Введите значение элемента: "))
# index = int(input("Введите индекс: "))
#
# def add_item_in_index(_list, index, a):
#     list_new = []
#     for i in range(index):
#         list_new.append(_list[i])
#     list_new.append(a)
#     for i in range(index, len(_list)):
#         list_new.append(_list[i])
#     return list_new
#
# print(add_item_in_index(list1, index, a))


# # 9.1 Используя готовые методы списков:
# # - Написать функцию, которая будет создавать список размером n и заполнять его числами в диапазоне от a до b.
#
# size = int(input("Введите размер списка: "))
# _min = int(input("Введите начало диапазона: "))
# _max = int(input("Введите конец диапазона: "))
#
# if _min>_max: _min, _max = _max, _min
#
# def create_random_list(size, _min, _max):
#     return [random.randint(_min, _max) for i in range(size)]
#
# list1 = create_random_list(size,_min, _max)
# print(list1)
#
#
# # 9.2 Написать функцию, принимает список и число и удаляет из списка все вхождения этого числа.
#
# num = int(input("Введите число на удаление: "))
#
# def remove_number (_list, num):
#     while num in _list:
#         _list.remove(num)
#     print(_list)


# remove_number(list1,num)