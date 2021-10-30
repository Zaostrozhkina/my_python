def int_func():
    """Возвращает слово с большой буквы"""
    word = input('Введите слово маленькими латинскими буквами: ')
    b = 0
    for a in word:
        if 97 <= ord(a) <= 122:
            b += 1
    if b == len(word):
        return word.capitalize()
    else:
        return 'Слово должно быть введено маленькими латинскими буквами без пробелов'


print(int_func())


def int_function():
    """Возвращает все слова с большой буквы"""
    list = input('Введите слова маленькими буквами через пробел: ').split()
    for word in list:
        b = 0
        for a in word:
            if 97 <= ord(a) <= 122:
                b += 1
        print(word.title() if b == len(word) else print('Слово должно быть введено маленькими латинскими буквами'))


int_function()
