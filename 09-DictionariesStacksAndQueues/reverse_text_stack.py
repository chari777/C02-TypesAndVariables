###
# Odwraca tekst za pomocą stosu: każdy znak odkładamy, a potem zdejmujemy od wierzchu.
#
import queue

def reverse_text(text):
    stack = queue.LifoQueue()
    for char in text:
        stack.put(char)
    # Zdejmowanie ze stosu odwraca kolejność znaków
    result = ''
    while not stack.empty():
        result += stack.get()
    return result

text = input('Enter text: ')
print('Reversed:', reverse_text(text))
