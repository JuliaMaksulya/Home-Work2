#Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.

n = []
n = int(input("Введите число N: "))
for i in range (-n,n+1):
    print (i,end=" ")
import math
print()
print(f"Произведение эллементов под индексом 0,2,3 \n{math.prod([0, 2, 3])}")
