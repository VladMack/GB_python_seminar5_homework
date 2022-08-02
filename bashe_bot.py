from random import randint


candys = 2021
players = ['Игрок', 'Бот']
player = players[randint(0, len(players) - 1)]
n = None
while candys > 0:
    n = 0
    if player == 'Игрок':
        player = 'Бот'
    else:
        player = 'Игрок'
    if player == 'Игрок':
        print(f'{player} ходит. Введи количество конфет:')
        while n not in range(1, 29) or n > candys:
            n = int(input())
    else:
        while n < 1 or n > candys:
            n = randint(1, 28)
    candys -= n
    print(f'{player} взял {n} конфет. Их осталось {candys}.')
    print()
print(f'{player} победил.')