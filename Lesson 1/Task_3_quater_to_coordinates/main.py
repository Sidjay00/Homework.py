"""
Задача 3. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат
точек в этой четверти (х и у).
1 -> x > 0, y > 0
"""

try:
    quater_number = int(input('Введите номер четверти: '))
except ValueError:
    print('Вы ввели не число')
    
if (quater_number < 1 or quater_number > 4):
    print(f"Вы ввели некорректный номер четверти. Введите цифры от 1 до 4!")
elif quater_number == 1:
    print(f"{quater_number} -> x > 0, y > 0")
elif quater_number == 2:
    print(f"{quater_number} -> x > 0, y < 0")
elif quater_number == 3:
    print(f"{quater_number} -> x < 0, y < 0")
else:
    print(f"{quater_number} -> x < 0, y > 0")   
