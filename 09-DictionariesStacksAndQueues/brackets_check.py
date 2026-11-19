# KROKI (na przykładzie "[(2+3)]"):
# '[' -> na stos.   '(' -> na stos.   '2','+','3' -> pomijamy (nie są nawiasami).
# ')' -> zdejmij '(' ze stosu, pasuje do ')'.   ']' -> zdejmij '[', pasuje.
# Na końcu stos pusty -> poprawne. Błąd: zamykający nawias nie pasuje do wierzchołka
# albo stos pusty przy zamknięciu, albo na końcu zostały otwarte nawiasy.
###
# Sprawdza, czy nawiasy (), {}, [] są poprawnie zagnieżdżone w wyrażeniu.
# Używamy stosu: otwierający nawias odkładamy, a zamykający musi pasować do wierzchu.
#
import queue

# Słownik: zamykający nawias -> pasujący otwierający
matching = {')': '(', ']': '[', '}': '{'}

def brackets_ok(expression):
    stack = queue.LifoQueue()
    for char in expression:
        # Otwierający nawias - odkładamy na stos
        if char in '([{':
            stack.put(char)
        # Zamykający nawias - musi pasować do ostatniego otwartego
        elif char in ')]}':
            # Stos pusty = zamknięcie bez otwarcia, np. ')'
            if stack.empty():
                return False
            # Zdejmujemy ostatni otwarty nawias i porównujemy
            if stack.get() != matching[char]:
                return False
    # Na koniec stos musi być pusty - inaczej zostały niezamknięte nawiasy
    return stack.empty()

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}"   # poprawne
expression2 = "[(2+3]/4)"                   # niepoprawne
expression3 = "(2-3*4+(5/6)"                # niepoprawne

for expression in [expression1, expression2, expression3]:
    if brackets_ok(expression):
        print(f'{expression} - brackets are correct')
    else:
        print(f'{expression} - brackets are NOT correct')
