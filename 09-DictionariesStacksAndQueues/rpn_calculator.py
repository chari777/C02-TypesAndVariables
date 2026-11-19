# KROKI na przykładzie '2 3 + ='
# 2 -> stos [2]; 3 -> stos [2,3]; '+' -> zdejmij 3 (b) i 2 (a), wynik 5 -> stos [5]
# '=' -> zdejmij wynik 5 i wypisz.
# Dlaczego b zdejmujemy pierwsze? Ostatnio dodana liczba to prawy argument działania.
# Dla '8 3 1 + / ...' działa tak samo: każdy operator zjada dwie liczby ze stosu.
###
# Kalkulator ONP (odwrotna notacja polska, RPN) oparty na stosie.
#   - liczba -> odkładamy na stos
#   - operator -> zdejmujemy dwie liczby, liczymy, wynik wracamy na stos
#   - znak '=' -> zdejmujemy wynik i wyświetlamy go
#
import queue

stack = queue.LifoQueue()
operators = ['+', '-', '*', '/']

print("Enter RPN tokens (numbers and operators separated by spaces). End with '='.")
print('Example: 2 3 + =')

finished = False
while not finished:
    # split() dzieli wiersz na osobne tokeny, więc można wpisać kilka naraz
    for token in input('> ').split():
        if token == '=':
            # Wynik zostaje na stosie jako jedyny element
            print('Result:', stack.get())
            finished = True
            break
        elif token in operators:
            # Operator wymaga dwóch argumentów. Najpierw zdejmujemy drugi (b), potem pierwszy (a),
            # bo kolejność ma znaczenie przy odejmowaniu i dzieleniu.
            b = stack.get()
            a = stack.get()
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            else:
                result = a / b
            stack.put(result)
        else:
            # Każdy inny token traktujemy jako liczbę
            stack.put(float(token))
