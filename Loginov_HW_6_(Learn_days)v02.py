days= int(input("Введите количество учебных дней в неделе: "))
count_hour=0
day_number = 1
while True:
    if 0 <= days <= 7:
        if days == 0:
            print ("Учебные дни закончились")
            break
        hours = int (input(f"Введите количество учебных часов в {day_number}-й день: "))
        if 0<= hours <= 24:
            count_hour += hours
            days -= 1
            day_number += 1
        else:
            print("Введите кол-во часов от 0 до 24")
    else:
        days= int(input("Введите количество учебных дней в неделе от 0 до 7: "))
print(f"На этой неделе вы занимались {count_hour} часов в течение {day_number-1} дней")