# Домашнее задание к занятию 1. Знакомство с Python  - задание 2
dates = []
tasks = []
i = 0
while i < 3:
    dateOfTask = input("Введите дату: ")
    dates.append(dateOfTask)
    taskname = input("Введите задачу: ")
    tasks.append(taskname)
    i = i + 1
i = 0
while i < 3:
    print(dates[i], tasks[i])
    i = i + 1