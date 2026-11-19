# KROKI:
# word_count: split() tnie zdanie po spacjach, len() liczy elementy.
# words_longest_first: sorted(..., key=len, reverse=True) - klucz to długość słowa.
# words_alphabetical: key=str.lower - sortuje bez względu na wielkość liter.
###
# Moduł MyText - funkcje do pracy z tekstem
#

# Liczba słów: split() dzieli tekst po spacjach na listę słów
def word_count(text):
    count = 0
    for _ in text.split():
        count += 1
    return count

# Słowa od najdłuższego do najkrótszego.
# sorted() z key=len sortuje według długości; reverse=True - malejąco.
def words_longest_first(text):
    return sorted(text.split(), key=len, reverse=True)

# Słowa alfabetycznie, bez rozróżniania wielkości liter.
# key=str.lower sprawia, że 'a' i 'A' są traktowane tak samo przy sortowaniu.
def words_alphabetical(text):
    return sorted(text.split(), key=str.lower)
