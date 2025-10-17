#1 Найти все уникальные элементы первого списка и вывести их на экран

list1= [1,12,52,1,31]
for i in range(len(list1)):
    flag = True
    for j in range(i):
        if list1[i] == list1[j]:
            flag= False
            break
    if flag:
        print(list1[i], end=" ")
print()

#2 Вывести все общие значения для двух списков без повтора

list1 = [1,12,52,1,31]
list2 = [2,12,4,5,34,1,5,3]
for i in range(len(list1)):
    flag=False
    for j in range(len(list2)):
        if list1[i] == list2[j]:
            flag=True
            break
    if flag:
        for j in range(i):
            if list1[i]==list1[j]:
                flag=False
                break
        if flag:
            print(list1[i], end =" ")
print()

#3 Все повторяющиеся значения первого списка заменить на 0

list1= [1,12,52,31,1]
for i in range(len(list1)):
    flag = False
    for j in range(len(list1)):
        if i!=j:
            if list1[i] == list1[j]:
                flag= True
                list1[j]=0
    if flag:
        list1[i] = 0
    print(list1[i], end=" ")
print()

#4 Определить в каком списке среднее значение элементов больше

list1 = [1,12,52,1,31]
list2 = [2,12,4,5,34,1,5,3]
avg1 = 0
summa1 = 0
avg2 = 0
summa2 = 0
for i in list1:
    summa1+=i
avg1=summa1/len(list1)
for j in list2:
    summa2+=j
avg2=summa2/len(list2)
if avg1>avg2:
    print("В первом")
elif avg2>avg1:
    print("Во втором")
else:
    print("Равны")

#5 Создать два списка одинакого размера но с разными значениями
#Поменять значения этих списков друг с другом в соответствии с их позициями

list1 = [1,12,52,1,31,1,4,45]
list2 = [2,12,4,5,34,1,5,3]
for i in range (len(list1)):
        list1[i],list2[i] = list2[i], list1[i]
print(list1)
print(list2)