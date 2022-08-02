def print_dict():
    print(f"{numbers['1']} {numbers['2']} {numbers['3']}")
    print(f"{numbers['4']} {numbers['5']} {numbers['6']}")
    print(f"{numbers['7']} {numbers['8']} {numbers['9']}")


def win_checker():
    if numbers['1'] == numbers['2'] == numbers['3'] \
            or numbers['4'] == numbers['5'] == numbers['6'] \
            or numbers['1'] == numbers['4'] == numbers['7'] \
            or numbers['7'] == numbers['8'] == numbers['9'] \
            or numbers['3'] == numbers['6'] == numbers['9'] \
            or numbers['1'] == numbers['5'] == numbers['9'] \
            or numbers['2'] == numbers['5'] == numbers['8'] \
            or numbers['3'] == numbers['5'] == numbers['7']:
        return True
    return False


player = 'o'


def switch_player():
    if player == 'o':
        player = 'x'
    else:
        player = 'o'


numbers = {'1': 1, '2': 2, '3': 3,
           '4': 4, '5': 5, '6': 6,
           '7': 7, '8': 8, '9': 9, }


while win_checker() == 0:
    # switch_player()
    if player == 'o':
        player = 'x'
    else:
        player = 'o'
    print_dict()
    print()
    coord = input(f'Ходят {player}. Введи номер ячейки:')
    print()
    numbers[coord] = player
print_dict()
print()
print(f'Победили {player}!')
