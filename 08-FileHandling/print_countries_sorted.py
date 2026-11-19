###
# Wczytuje cały plik countries.txt i wypisuje kraje posortowane alfabetycznie
#
def read_from_file(name):
    # encoding='utf-8' - bezpieczne dla polskich znaków w nazwach plików i treści
    with open(name, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

file_content = read_from_file('countries.txt')

# splitlines() dzieli tekst na listę linii i usuwa znaki nowej linii
file_lines = file_content.splitlines()

# sorted() zwraca nową, posortowaną listę (alfabetycznie, od A do Z)
for line in sorted(file_lines):
    print(line)
