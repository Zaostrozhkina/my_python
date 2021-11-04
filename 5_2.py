with open('file_for_5_2.txt', 'r', encoding='utf-8') as file:
    amount = len(file.readlines())
    print(f'Количество строк = {amount}')

    file.seek(0)

    list_line = file.readlines()
    i = 1
    for line in list_line:
        amount_word = len(line.split())
        print(f'Количество слов в строке {i} = {amount_word}')
        i += 1
