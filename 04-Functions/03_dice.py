###
# Generuje i wypisuje losową liczbę od 1 do 6 - jak rzut kostką
#
# Moduł random zawiera funkcje do losowania.
import random

# randint(a, b) losuje liczbę całkowitą z przedziału <a, b>, włącznie z końcami
dice_result = random.randint(1, 6)
print('Dice roll result:', dice_result)
