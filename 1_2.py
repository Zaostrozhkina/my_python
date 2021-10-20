time = int(input('Введите время к секундах: '))

if time < 60:
    print(f'00:00:{time:02}')
elif time >= 60 and time < 3600:
    minutes = time // 60
    seconds = time % 60
    print(f'00:{minutes:02}:{seconds:02}')
elif time >= 3600:
    hours = time // 3600
    minutes = time % 3600 // 60
    seconds = time % 60
    print(f'{hours:02}:{minutes:02}:{seconds:02}')
