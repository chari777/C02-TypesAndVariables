###
# Program testujący funkcje wbudowane (built-in) języka Python
#
# Funkcje wbudowane są dostępne od razu, bez importowania.
# Wywołanie funkcji = jej nazwa + nawiasy z argumentami.

# max() zwraca największą liczbę spośród podanych argumentów
max_number = max(7, 5, 6, 3, 8, 2)
print('Max number of 7,5,6,3,8,2 is', max_number)

# min() zwraca najmniejszą liczbę
min_number = min(4, 7, 2, 3, 9, 8)
print('Min number of 4,7,2,3,9,8 is', min_number)

# len() zwraca liczbę znaków w napisie (spacja też się liczy)
str_length = len("computer science")
print('The number of characters in "computer science" is', str_length)

# input() czyta tekst z klawiatury. Zawsze zwraca NAPIS (string),
# nawet jeśli wpiszemy same cyfry.
letter = input('Enter a letter: ')
print('Letter read from the keyboard:', letter)

# int(napis) zamienia napis zawierający cyfry na liczbę całkowitą.
# Bez tej zamiany "20303" zostałoby tylko tekstem.
number_from_string = int("20303")
print('Number representing the string "20303" is', number_from_string)

# bin() zamienia liczbę dziesiętną na napis z zapisem binarnym.
# Napis zaczyna się od '0b' - to znacznik, że to liczba binarna.
binary_string = bin(304)
print('Binary string representing decimal 304 is', binary_string)

# hex() robi to samo dla systemu szesnastkowego. Prefiks to '0x'.
hex_string = hex(304)
print('Hexadecimal string representing decimal 304 is', hex_string)

# ord() zwraca kod Unicode znaku. Znak € ma kod 8364.
unicode_code = ord('€')
print('Unicode code of the € sign is', unicode_code)

# abs() zwraca wartość bezwzględną, czyli liczbę bez znaku minus.
absolute_value = abs(-17)
print('Absolute value of -17 is', absolute_value)
