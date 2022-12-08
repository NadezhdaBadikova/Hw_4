# 2'. Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
# * 6 -> [2,3]
# * 144 -> [2,3]

import os
os.system('cls||clear')

num = int(input("Введите число: "))
i = 2
lst = []
old = num
while i <= num:
    if num % i == 0:
        lst.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {old} приведены в списке: {lst}")