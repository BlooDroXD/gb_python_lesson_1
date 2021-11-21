if __name__ == '__main__':
    try:
        now = int(input('Введите текущее количествокилометров: '))
        need = int(input('Введите необходимое количество километров: '))
        day = 0
        while True:
            if now < need:
                if day != 0:
                    day = day + 1
                    now = now + (now / 100*10)
                    print(f'{day}-й день: {now:0.2f}')
                else:
                    day = day + 1
                    print(f'{day}-й день: {now:0.2f}')
            else:
                print(f'на {day}-й день спортсмен достиг результата — не менее {need} км.')
                break

    except ValueError:
        print('Введено не верное значение, работа программы прекращена')