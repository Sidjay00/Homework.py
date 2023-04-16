DayOfWeek = int(input('Введите число, обозначающее день недели: '))

condition8 = DayOfWeek < 1
condition9 = DayOfWeek > 7
condition1 = DayOfWeek == 1
condition2 = DayOfWeek == 2
condition3 = DayOfWeek == 3
condition4 = DayOfWeek == 4
condition5 = DayOfWeek == 5
condition6 = DayOfWeek == 6

if (condition8 or condition9):
    print(f"Вы ввели некорректный день недели. Введите цифры от 1 до 7!")
elif condition1:
    print(f"{DayOfWeek} -> Понедельник")
elif condition2:
    print(f"{DayOfWeek} -> Вторник")
elif condition3:
    print(f"{DayOfWeek} -> Среда")
elif condition4:
    print(f"{DayOfWeek} -> Четверг")
elif condition5:
    print(f"{DayOfWeek} -> Пятница")
elif condition6:
    print(f"{DayOfWeek} -> Суббота")
else:
    print(f"{DayOfWeek} -> Воскресенье")    