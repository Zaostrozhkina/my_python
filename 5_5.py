with open('file_for_5_5.txt', 'w+', encoding='utf-8') as file:
    file.writelines(input('Введите числа через пробел: '))
    file.seek(0)
    print(sum(map(int, file.readline().split())))
