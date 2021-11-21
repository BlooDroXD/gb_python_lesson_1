if __name__ == '__main__':
    try:
        seconds = int(input('Введите количество секунд: '))
        if (seconds < 86400):
            hour = int(seconds / 3600)
            minute = int((seconds - hour * 3600) / 60)
            sec = int((seconds - hour * 3600) - minute * 60)
            print("{hours:d}:{minutes:d}:{secs:d}".format(hours=hour, minutes=minute, secs=sec))
        else:
            print(f'Вы ввели в секундах более 1 суток.')
    except ValueError:
        print('Введено не верное значение, работа программы прекращена')