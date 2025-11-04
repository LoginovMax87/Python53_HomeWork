employees = []

def show_employees():
    if not employees:
        print("Список сотрудников пуст")
        return
    header = ["№", "Фамилия", "Имя", "Отчество", "Кабинет", "Телефон", "Должность"]
    for h in header:
        print(f"{h}\t|", end="")
    print()
    for i in range(len(employees)):
        print(i + 1, end="\t| ")
        for j in range(len(employees[i])):
            print(employees[i][j], end="\t| ")
        print()
    print()


def add_employee():
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    office = input("Введите номер кабинета: ")
    phone = input("Введите номер телефона: ")
    position = input("Введите должность: ")
    employees.append([surname, name, patronymic, office, phone, position])
    print("Сотрудник добавлен")


def delete_employee():
    show_employees()
    num = int(input("Введите номер сотрудника для удаления: "))
    if 1 <= num <= len(employees):
        employees.pop(num - 1)
        print("Сотрудник удалён")
    else:
        print("Такого сотрудника нет")


def find_by_office():
    office = input("Введите номер кабинета: ")
    found = False
    for emp in employees:
        if emp[3] == office:
            print(emp)
            found = True
    if not found:
        print("В этом кабинете нет сотрудников")


def get_surname(emp):
    return emp[0]


def sort_by_surname():
    employees.sort(key=get_surname)
    print("Список отсортирован по фамилии")


def find_by_surname():
    surname = input("Введите фамилию: ")
    found = False
    for emp in employees:
        if emp[0].lower() == surname.lower():
            print(emp)
            found = True
    if not found:
        print("Сотрудник не найден")


def edit_employee():
    show_employees()
    num = int(input("Введите номер сотрудника для изменения: "))
    if 1 <= num <= len(employees):
        emp = employees[num - 1]
        print(f"Редактирование данных сотрудника: {emp[0]} {emp[1]} {emp[2]}")
        fields = ["Фамилия", "Имя", "Отчество", "Кабинет", "Телефон", "Должность"]
        for i in range(len(fields)):
            new_value = input(f"{fields[i]} ({emp[i]}): ")
            if new_value.strip() != "":
                emp[i] = new_value
        print("Данные сотрудника обновлены")
    else:
        print("Некорректный номер")


while True:
    choice = int(input(
        '''
        Меню:
        1. Показать всех сотрудников
        2. Добавить сотрудника
        3. Удалить сотрудника
        4. Найти по кабинету
        5. Сортировать по фамилии
        6. Найти по фамилии
        7. Изменить данные сотрудника
        8. Выход
        '''
    ))

    match choice:
        case "1":
            show_employees()
        case "2":
            add_employee()
        case "3":
            delete_employee()
        case "4":
            find_by_office()
        case "5":
            sort_by_surname()
        case "6":
            find_by_surname()
        case "7":
            edit_employee()
        case "0":
            print("Выход из программы...")
            break
        case _:
            print("Неверный ввод, попробуйте снова")