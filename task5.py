#Реализуйте алгоритм перемешивания списка.

import random
from random import randint
lis = []
for i in range(10):
    lis.append(randint(0, 10,))
print(f"изначальный список {lis}")
random.shuffle(lis)
print(f"перемешанный список {lis}")