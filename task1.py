# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

num = input("введите число: ")
str_num = str(num)
str_num = str_num.replace('.', '')
lst_str = list(str_num)
lst_num = map(int, lst_str)
s = sum(lst_num)
print(s)




