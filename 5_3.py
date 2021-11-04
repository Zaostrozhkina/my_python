with open('text_3.txt', 'r', encoding='utf-8') as file:
    list = file.readlines()

    less_20 = [line.split()[0] for line in list if float(line.split()[1]) < 20000]
    print(f'Сотрудники с окладом менее 20 тысяч: {less_20}')

    salary = [float(line.split()[1]) for line in list]
    medium_salary = sum(salary) / len(salary)
    print(f'Средняя заработная плата равна {medium_salary}')
