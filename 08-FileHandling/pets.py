###
# Wypisuje tekst z pliku pets.txt i liczy słowa w nim zawarte
#
with open('pets.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()   # readlines() zwraca listę wszystkich linii

words_total = 0
for line in lines:
    # Wypisujemy linię bez dodatkowego znaku nowej linii (end="" - linia już go ma)
    print(line, end="")
    # split() dzieli linię po spacjach na listę słów, len() liczy te słowa
    words_total += len(line.split())

print()
print('Number of words in the text:', words_total)
