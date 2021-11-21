if __name__ == '__main__':
    try:
        firststring = input('Введите первую строку: ')
        secondstring = input('Введите вторую строку: ')
        firstnumber = int(input('Введите перове число: '))
        secondnumber = int(input('Введите второе число: '))
        print(f'Первая строка : {firststring}, вторая строка: {secondstring} ,'
              f'Первое число: {firstnumber}, второе число: {secondnumber}')
    except ValueError:
        print('Введено не верное значение, работа программы прекращена')