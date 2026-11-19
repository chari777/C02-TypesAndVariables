###
# Wypisuje planszę kółko-krzyżyk (3x3)
# Plansza to lista list - każdy wewnętrzny element to jeden wiersz.
#
tic_tac_toe_board = [
    ['X', 'O', 'X'],
    [' ', 'X', 'O'],
    ['O', ' ', 'X']
]

# Zewnętrzna pętla przechodzi po wierszach
for row in tic_tac_toe_board:
    # Wewnętrzna pętla przechodzi po polach w wierszu
    for cell in row:
        # end=" " - nie przechodzimy do nowej linii, tylko dodajemy spację
        print(cell, end=" ")
    # Pusty print() kończy wiersz i przechodzi do następnego
    print()
