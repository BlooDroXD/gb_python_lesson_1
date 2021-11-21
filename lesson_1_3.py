if __name__ == '__main__':
    try:
        number = int(input('Введите цифру: '))
        summ = 0
        temp = number
        if number < 10:
            for i in range(3):
                summ = summ + temp
                temp = temp * 10 + number
            print(f"{summ:d}")
        else:
            print(f'Вы ввели в не цифру')
    except ValueError:
        print('Введено не верное значение, работа программы прекращена')