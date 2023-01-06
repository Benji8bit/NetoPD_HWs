# Домашнее задание к занятию 1. Знакомство с Python - задание 3
myTasks = {}
i = 0
while i < 3:
    dateOfTask = input("Введите дату: ")
    taskname = input("Введите задачу: ")
    myTasks[dateOfTask] = taskname
    i = i + 1

print(myTasks)