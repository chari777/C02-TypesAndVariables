# KROKI:
# 1. Dla każdej nazwy pliku szukamy OSTATNIEJ kropki (rfind).
# 2. Rozszerzenie to tekst po kropce: 'meeting_notes.html' -> 'html'.
# 3. Jeśli rozszerzenie ma dokładnie 4 znaki -> wypisujemy nazwę.
# 4. Plik bez kropki (rfind zwraca -1) pomijamy: continue.
###
# Wypisuje tylko te nazwy plików, których rozszerzenie ma dokładnie 4 znaki (np. html)
#
with open('files.txt', 'r', encoding='utf-8') as file:
    for line in file:
        name = line.strip()   # usuwamy znak nowej linii z końca
        # rfind('.') znajduje ostatnią kropkę; rozszerzenie to wszystko po niej
        dot_position = name.rfind('.')
        if dot_position == -1:
            continue   # brak kropki = brak rozszerzenia, pomijamy plik
        extension = name[dot_position + 1:]
        if len(extension) == 4:
            print(name)
