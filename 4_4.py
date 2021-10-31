from random import randint

list_1 = [randint(1, 15) for _ in range(15)]
list_2 = [n for n in list_1 if list_1.count(n) == 1]
print(list_1)
print(list_2)
