if __name__ == '__main__':
    try:
        number = int(input('Введите число: '))
        max = 0
        arofnum = [int(a) for a in str(number)]
        for i in range(len(arofnum)):
            if arofnum[i] > max:
                max = arofnum[i]
        print(max)
    except ValueError:
        print('Введено не верное значение, работа программы прекращена')