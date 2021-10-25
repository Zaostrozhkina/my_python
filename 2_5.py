list = [8, 8, 7, 5, 4, 3, 3, 3, 1]
number = float(input('Введите натуральное число: '))
i = 0
for n in list:
    if n >= number:
        i += 1
    else:
        break
list.insert(i, number)
print(list)
