number = int(input('Введите целое положительное число: '))
maxi = 0
while number > 0:
    a = number % 10
    if a >= maxi:
        maxi = a
    number //= 10
print(maxi)




