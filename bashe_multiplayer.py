candys = 2021
player = 'второй'
while candys > 0:
    n = 0
    if player == 'первый':
        player = 'второй'
    else:
        player = 'первый'
    print(f'Ходит {player} игрок. Введи количество конфет:')
    while n not in range(1, 29) or n > candys:
        n = int(input())
    candys -= n
    print(f'{player} игрок взял {n} конфет. Их осталось {candys}.')
    print()
print(f'Победил {player} игрок.')