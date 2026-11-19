###
# Program wypisujący nazwę miesiąca dla podanego numeru.
# Funkcję month importujemy z modułu months.py.
from months import month

# Przykład ze zadania: 'Enter month number: 9' -> 'The name of month 9 is September'
number = int(input('Enter month number: '))
print(f'The name of month {number} is {month(number)}')
