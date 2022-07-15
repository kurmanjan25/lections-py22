# Тип данных int()
# number = 5 # numer - переменная
# # +
# a = 10
# b = 5
# result = a + b
# print(result)
# print (a+100)



# a = 10
# b = 60
# c = 100
# d = 1000000
# e = 50
# print(a+b+c+d+e)

# / and // 
# 5 / 2 = 2.5 -> float()
# 5 // 2 = 2 -> целочисленное деление

# num1 = 25
# num2 = 12
# print(num1 / num2)
# print(num1 // num2)

# *
# % -> деление при котором мы получим остаток
# a = 5
# b = 2
# result = a % b
# print(result)

# ** -> возведение в степень pow()
# 5 ** 4 = 625
# 5 ** 2 = 25
# print(2 ** 4)

# a = 5
# b = 3
# result = pow (a, 5)
# print(result)
# print(pow(a, b))
# print (pow(5, 2, 12))

# round() -> округление числа с плавающей точкой

# a = 5.728232
# result = round(a, 2)
# print(result)

# abs() -> абсолютное значение -> abs(-5) -> 5
# |-5| = 5

# a = abs(-16)
# print(a)

# divmode(a, b) -> выводит два числа, первое число это результат целочисленного деления(//) a на b. Второе число это модульное деление(%) a на b.
# result = divmod(5, 2)
# print(result)

# import math

# a = 5
# print(math.sqrt(a))

# chislo_pi = math.pi
# print(chislo_pi)

# Множественное присваивание
# оператор присваивания (=)

# a, b, c = 1, 2, 5
# print(a, b, c)

# a, b, c = c, a, b 
# print(a, b, c)

from math import pi

r = int(input('Vvedite radius: '))
result_P = 2 * r * pi
result_S = pi * (r ** 2)
print('Площадь окружности', round(result_S, 2))
print('Периметр окружности', round(result_P, 2))
