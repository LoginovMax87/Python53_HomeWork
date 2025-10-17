# 1 написать функцию генерирующую список заданного размера из случайных значений заданного диапазона
import random
size = int(input("Введите количество элементов списка: "))
_min = int(input("Введите начало диапазона: "))
_max = int(input("Введите конец диапазона: "))

def create_random_list(size, _min, _max):
    _list = []
    for i in range(size):
        _list.append(random.randint(_min, _max))
    return _list

list1 = create_random_list(size, _min, _max)
print(list1)