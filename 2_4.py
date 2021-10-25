str = input('Введите строку из нескольких слов через пробел: ').split()
for n, word in enumerate(str, 1):
    print(n, '-', word[:10])
