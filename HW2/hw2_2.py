HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи.
exit - выход из программы."""

tasks = []
today = []
tomorrow = []
other = []

run = True

while run:
    command = input("Введите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        print(tasks)
    elif command == "add":
        taskdate = input("Вы хотите добавить задачу на сегодня, завтра или на другой день?")
        task = input("Введите название задачи: ")
        if taskdate == "Сегодня":
            today.append(task)
        elif taskdate == "Завтра":
            tomorrow.append(task)
        else:
            other.append(task)
        print("Задача добавлена в список")
    elif command == "exit":
        print("Спасибо за использование! До свидания!")
        break
    else:
        print("Неизвестная команда")
        break

print("До свидания!")