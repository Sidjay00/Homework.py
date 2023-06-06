"""
Задача 1. Создайте пользовательский аналог метода map().
"""

# def my_map(func, numbers):
#     return(el for el in numbers if func(el))

# numbers = [1, 14, 6, 10, 3, 2, 5]

# # print(list(filter(lambda x: x > 5, numbers)))

# print(list(my_map(lambda x: x > 5, numbers)))


def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

data = [1,2,3,5,8,15,23,38]
res = select(int, data)
print(data)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(select(lambda x: (x, x ** 2), res))
print(res)