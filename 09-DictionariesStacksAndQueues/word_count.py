###
# Zlicza, ile razy każde słowo występuje w akapicie
#
paragraph = "cat dog mouse cat rat cat mouse"

counts = {}
# split() dzieli akapit na listę słów po spacjach
for word in paragraph.split():
    # Jeśli słowa nie ma jeszcze w słowniku, dodajemy je z licznikiem 0.
    # get(word, 0) zwraca wartość albo 0, gdy klucza brak - bezpieczniej niż word in counts.
    counts[word] = counts.get(word, 0) + 1

for word, count in counts.items():
    print(f'{word}: {count}')
