if __name__ == '__main__':
    try:
        gain = int(input('Введите выручку: '))
        costs = int(input('Введите издержки: '))
        if gain > costs:
            print('Фирма работает с прибылью')
            rent = gain - costs
            personal = int(input('Введите количество персонала: '))
            print('Выручка фирмы на человека = {cost:.2f}'.format(cost=rent/personal))
        else:
            print('Фирма работает в убыток')
    except ValueError:
        print('Введено не верное значение, работа программы прекращена')