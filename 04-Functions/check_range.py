###
# Program sprawdza, czy liczba należy do przedziału <2, 15>
from number_tools import in_range

number = int(input('A number: '))
# Wynik funkcji to True/False, więc zamieniamy go na 'yes' lub 'no'
answer = 'yes' if in_range(number, 2, 15) else 'no'
print(f'Number {number} in the range <2,15>: {answer}')
