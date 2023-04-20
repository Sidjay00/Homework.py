"""
Задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и выводит название этого дня недели.
1 –> Понедельник
10 –> Нет такого дня
7 –> Воскресение
"""

DayOfWeek = int(input('Введите число, обозначающее день недели: '))

if (DayOfWeek < 1 or DayOfWeek > 7):
    print(f"Вы ввели некорректный день недели. Введите цифры от 1 до 7!")
elif DayOfWeek == 1:
    print(f"{DayOfWeek} -> Понедельник")
elif DayOfWeek == 2:
    print(f"{DayOfWeek} -> Вторник")
elif DayOfWeek == 3:
    print(f"{DayOfWeek} -> Среда")
elif DayOfWeek == 4:
    print(f"{DayOfWeek} -> Четверг")
elif DayOfWeek == 5:
    print(f"{DayOfWeek} -> Пятница")
elif DayOfWeek == 6:
    print(f"{DayOfWeek} -> Суббота")
else:
    print(f"{DayOfWeek} -> Воскресенье")    