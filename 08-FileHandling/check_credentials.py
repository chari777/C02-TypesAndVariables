# KROKI:
# 1. Wczytujemy login i hasło z klawiatury.
# 2. Wzorzec ^...$ musi pasować do CAŁEGO napisu (od początku do końca).
# 3. Login: [a-z]{6,} - tylko małe litery, minimum 6.
# 4. Hasło: [A-Za-z0-9_]{8,} - litery, cyfry, _, minimum 8.
# 5. Jeśli oba pasują -> komunikat OK; inaczej mówimy, co jest źle.
###
# Sprawdza, czy login i hasło spełniają wymagania:
#   login: min. 6 znaków, tylko małe litery
#   hasło: min. 8 znaków, tylko litery, cyfry i znak '_'
#
import re

username = input('Username: ')
password = input('Password: ')

# ^ - początek tekstu, $ - koniec tekstu, dzięki temu sprawdzamy CAŁY napis
# [a-z] - małe litery, {6,} - co najmniej 6 razy
username_pattern = r'^[a-z]{6,}$'
# [A-Za-z0-9_] - litery (małe i duże), cyfry i podkreślenie, {8,} - co najmniej 8
password_pattern = r'^[A-Za-z0-9_]{8,}$'

# re.match sprawdza dopasowanie od początku tekstu; None oznacza brak dopasowania
username_ok = re.match(username_pattern, username) is not None
password_ok = re.match(password_pattern, password) is not None

if username_ok and password_ok:
    print('Username and password are correct.')
else:
    if not username_ok:
        print('Username must have at least 6 lowercase letters.')
    if not password_ok:
        print('Password must have at least 8 characters: letters, digits or _.')
