###
# Moduł z funkcją maskującą numer karty płatniczej
#
def hide(card_number):
    # Z numeru zostają tylko pierwsze 2 i ostatnie 4 cyfry.
    # Środek zamieniamy na gwiazdki: liczba gwiazdek to długość minus 6.
    # Napis '*' * n tworzy napis złożony z n gwiazdek.
    hidden_count = len(card_number) - 6
    return card_number[:2] + '*' * hidden_count + card_number[-4:]
