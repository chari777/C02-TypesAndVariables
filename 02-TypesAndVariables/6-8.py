first = input('Enter first letter: ')
last = input('Enter last letter: ')

first_letter_code = ord(first) # zamieniam pierwszą literę na jej numer (np. A -> 65)
last_letter_code = ord(last)   # zamieniam drugą literę na jej numer (np. D -> 68)

# odejmuję numery i odejmuję 1, żeby nie policzyć samej litery końcowej (68 - 65 - 1 = 2)
# używam max(0, ...), żeby dla tych samych liter (np. K i K) wyszło 0 zamiast -1
number_of_letters = max(0, last_letter_code - first_letter_code - 1)
print(f'Between {first} and {last} is {number_of_letters} letters')