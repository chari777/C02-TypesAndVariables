###
# Krotki (tuple) - niezmienialne, uporządkowane kolekcje elementów.
# Krotka tworzy się w nawiasach (), a nie []
#

# Krotka z jednym elementem MUSI mieć przecinek na końcu.
# Bez przecinka ('computation') Python uznałby to za zwykły napis.
word_tuple = ('computation',)
print('Tuple:', word_tuple)
print('Type of the variable:', type(word_tuple))

# Odwrócenie krotki: krok -1 w wycinku [::-1]
numbers = (10, 20, 30, 40, 50)
print('Tuple:', ','.join(map(str, numbers)))
print('Reverse order:', ','.join(map(str, numbers[::-1])))

# Krotka może zawierać różne typy - tu napis, listę i inną krotkę
mixed = ("Seven", [10, 20, 30], (5, 15, 25))
print(mixed[0])        # "Seven"
print(mixed[1][2])     # 30 - trzeci element listy w środku

# count() zlicza, ile razy wartość występuje w krotce
values = (50, 20, 40, 50, 30, 50)
value = 50
print('Tuple:', ','.join(map(str, values)))
print('Value:', value)
print('Number of occurrences:', values.count(value))
