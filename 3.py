# 3'. Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.

import os
os.system('cls||clear')

arrayList = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходный список: {arrayList}")
newArrayList = []
[newArrayList.append(i) for i in arrayList if i not in newArrayList]
print(f"Список из неповторяющихся элементов: {newArrayList}")