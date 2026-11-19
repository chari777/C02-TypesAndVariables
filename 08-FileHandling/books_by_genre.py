# KROKI:
# 1. csv.reader czyta plik wiersz po wierszu, każdy wiersz to lista pól.
# 2. next(reader) pomija nagłówek i zapisuje go pierwszy do pliku wynikowego.
# 3. row[2] to kolumna 'Genre' (indeksy od 0: Title=0, Author=1, Genre=2).
# 4. Pasujące wiersze trafiają do pliku przez csv.writer.
###
# Kopiuje dane książek z pliku books.csv do osobnych plików według gatunku.
# Każdy gatunek ma swój plik, np. Fantasy -> books_fantasy.txt
#
import csv

# Mapowanie gatunek -> nazwa pliku wynikowego
genre_files = {
    'Fantasy': 'books_fantasy.txt',
    'Historical': 'books_historical.txt',
    'Romance': 'books_romance.txt',
    'Classic': 'books_classic.txt',
}

# Kopiuje wiersze z podanym gatunkiem do pliku.
def copy_genre(source_file, genre, target_file):
    with open(source_file, 'r', encoding='utf-8', newline='') as source:
        reader = csv.reader(source)
        # Pierwszy wiersz to nagłówek - kopiujemy go tylko raz, jako pierwszy
        header = next(reader)
        count = 0
        with open(target_file, 'w', encoding='utf-8', newline='') as target:
            # lineterminator='\n' - zapis z końcem linii w stylu Unix (bez \r)
            writer = csv.writer(target, lineterminator='\n')
            writer.writerow(header)
            for row in reader:
                # Trzecia kolumna (indeks 2) to gatunek
                if row[2] == genre:
                    writer.writerow(row)
                    count += 1
    return count

# Dla każdego gatunku z mapy tworzymy osobny plik
for genre, target in genre_files.items():
    copied = copy_genre('books.csv', genre, target)
    print(f'{genre}: {copied} books -> {target}')
