mounth = int(input())
match mounth:
    case 1 | 2 | 12:
        print('Зима')
    case 3 | 4 | 5:
        print('Весна')
    case 6 | 7 | 8:
        print('Лето')
    case 9 | 10 | 11:
        print('Осень')
    case _:
        print('Ошибка')
