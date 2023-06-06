import random

number = random.randint(1, 1000)
# print(number)

user_number = 0
count = 1

def func(u_num, num, count):
    while u_num != num:    
        u_num = int(input('Угадайте число. Введите число от 1 до 1000: '))
        if u_num == num:
            print(f'Вы отгадали число за {count} раз!')
        elif u_num > num:
            print('Указанное вами число больше загаданного.')
            count = count + 1
        else:
            print('Указанное вами число меньше загаданного.')
            count = count + 1
    
func(user_number, number, count)
    