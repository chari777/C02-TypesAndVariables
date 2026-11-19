###
# Program maskuje numer karty kredytowej.
# Funkcję hide importujemy z modułu card.py.
from card import hide

card_number = '5290312400019022'
print(f'f("{card_number}") returns "{hide(card_number)}"')
