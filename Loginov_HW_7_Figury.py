#Ромб
while True:
    n = int(input("Введите высоту ромба (нечётное число, например, 7)): "))
    if n%2!=0:
        break
    print("Вы ввели чётное число")
for i in range(n // 2 + 1):
    for j in range((n // 2) - i):
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")
    print()
for i in range((n // 2) - 1, -1, -1):
    for j in range((n // 2) - i):
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")
    print()

#Песочные часы
while True:
    n = int(input("Введите высоту часов (нечётное число, например, 7)): "))
    if n%2!=0:
        break
    print("Вы ввели чётное число")
for i in range(n // 2 + 1):
    for j in range(i):
        print(" ", end="")
    for j in range(n - 2 * i):
        print("*", end="")
    print()
for i in range((n // 2) - 1, -1, -1):
    for j in range(i):
        print(" ", end="")
    for j in range(n - 2 * i):
        print("*", end="")
    print()


#Перевернутые песочные часы
while True:
    n = int(input("Введите ширину часов (нечётное число, например, 7)): "))
    if n%2!=0:
        break
    print("Вы ввели чётное число")
for i in range(n // 2):
    for j in range(i + 1):
        print("*", end="")
    for j in range(n - 2 * (i + 1)):
        print(" ", end="")
    for j in range(i + 1):
        print("*", end="")
    print()
for j in range(n):
    print("*", end="")
print()
for i in range(n // 2 - 1, -1, -1):
    for j in range(i + 1):
        print("*", end="")
    for j in range(n - 2 * (i + 1)):
        print(" ", end="")
    for j in range(i + 1):
        print("*", end="")
    print()