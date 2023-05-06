"""
Задача 1. Создайте список. Запишите в него N первых элементов последовательности Фибоначчи.
6 –> 1 1 2 3 5 8 
"""

try:
    length = int(input('Введите число элементов последовательности: '))
except ValueError:
    print('Вы ввели не число!')
    exit()
fibonacci = [0] * length

if length <= 0:
    print('Число элементов не может быть меньше или равно 0!')
    exit()
elif length == 1:
    fibonacci = 0
elif length >= 2:
    fibonacci[0] = 0
    fibonacci[1] = 1
    for index in range(2, length):
        fibonacci[index] = fibonacci[index - 1] + fibonacci[index - 2]
        
    

print(f'{length} -> {fibonacci}')