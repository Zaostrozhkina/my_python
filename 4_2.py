list_1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
list_2 = [list_1[n] for n in range(1, len(list_1)) if list_1[n] > list_1[n - 1]]
print(list_2)
