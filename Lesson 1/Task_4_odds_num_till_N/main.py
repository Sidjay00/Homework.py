"""
Задача 4. Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.
5 -> 2, 4
8 -> 2, 4, 6, 8
"""

try:
    N = int(input('Введите натуральное число N: '))
except ValueError:
    print('Вы ввели не число!')

value = 2
print(f'{N} -> ', end='')
while value <= N:
    if value % 2 == 0:
        print(f'{value}, ', end='')
    value = value +1