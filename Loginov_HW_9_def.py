# 1 написать функцию генерирующую список заданного размера из случайных значений заданного диапазона
import random
size = int(input("Введите количество элементов списка: "))
_min = int(input("Введите начало диапазона: "))
_max = int(input("Введите конец диапазона: "))
def create_random_list(size, _min, _max):
    if _min > _max:
        _min,_max=_max,_min
    _list = []
    for i in range(size):
        _list.append(random.randint(_min, _max))
    return _list

list1 = create_random_list(size, _min, _max)
print(list1)




#2 написать функцию, возвращающую максимальное значение из списка
list1 = [1,12,52,1,31,10,123]

def max_item(_list):
    _maximum=_list[0]
    for i in range (1,len(_list)):
        if list1[i]>_maximum:
            _maximum=_list[i]
    print(_maximum)

max_item(list1)


# 3. написать функцию, определяющую количество повторяющихся значений списка

list1 = [1,12,52,1,31,10,123,1,10]

def rep_count(_list):
    rep = 0
    for i in range(len(_list)):
        flag = False
        for j in range(i):
            if _list[i] == _list[j]:
                flag = True
                break

        if flag == False:
            count = 0
            for j in range(len(_list)):
                if _list[i] == _list[j]:
                    count += 1
            if count > 1:
                rep += 1

    print(rep)

rep_count(list1)


# 4. написать функцию, принимающую в качестве параметра список и
# возвращающую новый список, включающий только положительные числа из
# первого списка

list1 = [1,12,-8,52,1,31,-8,10,123,1,10,-11]

def positive_number(_list):
    list_positive = []
    for i in range(len(_list)):
        if _list[i] > 0:
            list_positive.append(_list[i])  # добавляем только положительные элементы
    return list_positive

list2 = positive_number(list1)
print(list2)
print(positive_number(list1))

# 5. написать функцию, удаляющую из списка все четные значения

list1 = [1,12,-8,52,1,31,-8,10,123,1,10,-11,0]

def even_numbers_rem(_list):
    odd_list = []
    for i in range(len(_list)):
        if _list[i] % 2 != 0:
            odd_list.append(_list[i])
    return odd_list

print(even_numbers_rem(list1))


# 6 написать функцию, принимающую два списка и возвращающую список содержащий все уникальные элементы из этих двух списков

list1 = [1,12,-8,52,1]
list2 = [2,12,4]

def uniq_items(_list1, _list2):

    list_uniq= []
    for i in range (len(_list1)):
        uniq = True
        for j in range (len(list_uniq)):
            if _list1[i] == list_uniq[j]:
                uniq = False
                break
        if uniq:
            list_uniq.append(_list1[i])
    for i in range(len(_list2)):
        uniq = True
        for j in range(len(list_uniq)):
            if _list2[i] == list_uniq[j]:
                uniq = False
                break
        if uniq:
            list_uniq.append(_list2[i])

    return list_uniq


print(uniq_items(list1, list2))