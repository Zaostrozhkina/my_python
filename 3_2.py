def f_date(year, city, name, surname, email, phone):
    print(
        f'Пользователь {name} {surname}, {year} года рождения. Проживает в городе {city}. Email: {email}. Телефон: {phone}')


f_date(name=input('Введите ваше имя: '), surname=input('Введите вашу фамилию: '),
       year=input('Введите ваш год рождения: '), city=input('Введите город проживания: '),
       email=input('Введите ваш email: '), phone=input('Введите ваш телефон: '))
