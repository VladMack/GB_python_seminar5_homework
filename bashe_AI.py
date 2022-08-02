from random import randint


candys = 50
players = ['Игрок', 'Бот']
player = players[randint(0, len(players) - 1)]
max_try = 7
n = 0
while candys > 0:
    if player == 'Игрок':
        player = 'Бот'
    else:
        player = 'Игрок'
    if player == 'Игрок':
        n = 0
        print(f'{player} ходит. Введи количество конфет:')
        while n not in range(1, max_try + 1) or n > candys:
            n = int(input())
    else:
        if max_try < candys:
            if n > 0:
                n = max_try + 1 - n
            else:
                n = max_try
        else:
            n = candys
    candys -= n
    print(f'{player} взял {n} конфет. Их осталось {candys}.')
    print()
print(f'{player} победил.')
