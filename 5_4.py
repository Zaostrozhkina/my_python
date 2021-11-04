with open('text_44.txt', 'w', encoding='utf-8') as file_new:
    with open('text_4.txt', 'r', encoding='utf-8') as file:
        dict_rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
        for line in file.readlines():
            file_new.writelines(line.replace(line.split()[0], dict_rus.get(line.split()[0])))
