math = 5
art = 4
music = 5
history = 3 # usunąłem cudzysłowy wokół '3', bo Python traktował to jako tekst, a nie liczbę

# dałem nawiasy wokół dodawania (bez nich podzieliłby tylko historię przez 4) i poprawiłem literówki w nazwach zmiennych
average = (math + art + music + history) / 4

# ujednoliciłem cudzysłowy na początku i końcu oraz poprawiłem literówkę w nazwie zmiennej 'average'
print("Average grade is", average)