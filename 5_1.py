with open('file_1.txt', 'w', encoding='utf-8') as file:
    while True:
        line = input('Введите данные: ')
        file.write(f'{line} \n')
        if not line:
            break
