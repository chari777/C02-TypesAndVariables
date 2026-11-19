# KROKI (każda funkcja wczytująca):
# 1. while True: pytamy, aż użytkownik poda poprawną wartość.
# 2. try: próbujemy zamienić napis na liczbę (int/float).
# 3. Jeśli się nie udało, except ValueError łapie błąd i pytamy ponownie.
# 4. Jeśli się udało, return kończy funkcję i zwraca wartość.
###
# Funkcje do wczytywania różnych typów danych z klawiatury.
#
# input() zawsze zwraca napis (string). Te funkcje zamieniają go
# na właściwy typ i pilnują, żeby program nie wywalił się przy złym wpisie.


# Zwraca napis wpisany z klawiatury (bez zmian)
def input_string(message):
    text = input(message)
    return text


# Zwraca liczbę całkowitą (int).
# Pętla while True działa, dopóki użytkownik nie wpisze poprawnej liczby.
# try/except łapie błąd ValueError, który pojawia się, gdy int() dostanie tekst
# niebędący liczbą (np. 'abc'), zamiast pozwolić programowi się zawiesić.
def input_integer(message):
    while True:
        text = input(message)
        try:
            value = int(text)
            return value
        except ValueError:
            print('Please enter an integer number.')


# Zwraca liczbę rzeczywistą (float). Działa tak samo jak input_integer,
# tylko używa float(), który przyjmuje też liczby z częścią ułamkową.
def input_real(message):
    while True:
        text = input(message)
        try:
            value = float(text)
            return value
        except ValueError:
            print('Please enter a real number.')


# Zwraca True dla 'y', False dla 'n'.
# Pętla powtarza pytanie, dopóki użytkownik nie naciśnie y lub n.
# .lower() zamienia Y na y, więc wielkość liter nie ma znaczenia.
def input_boolean(message):
    while True:
        answer = input(message).strip().lower()
        if answer == 'y':
            return True
        if answer == 'n':
            return False
        print('Please press y or n.')
