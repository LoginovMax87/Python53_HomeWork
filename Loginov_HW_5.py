player = input("Введите камень, ножницы или бумага: ")
import random
a=random.randint(0,2)
if player == "камень":
    if a==0:
        print("камень - ничья")
    elif a==1:
        print("ножницы - вы выиграли")
    else:
        print("бумага - вы проиграли")
if player == "ножницы":
    if a==0:
        print("камень - вы проиграли")
    elif a==1:
        print("ножницы - ничья")
    else:
        print("бумага - вы выиграли")
if player == "бумага":
    if a == 0:
        print("камень - вы выиграли")
    elif a == 1:
        print("ножницы - вы проиграли")
    else:
        print("бумага - ничья")
