###
# Stos (LIFO) - odkładamy liczby na stos i zdejmujemy je z wierzchu.
# Używamy queue.LifoQueue, czyli kolejki działającej jak stos.
#
import queue

stack = queue.LifoQueue()

# put() odkłada element na wierzch stosu
for number in [2, 3, 7, 4, 1, 9, 8]:
    stack.put(number)

# Suma dwóch ostatnich liczb: zdejmujemy dwa elementy z wierzchu stosu.
# get() zwraca wierzchni element i usuwa go ze stosu.
last = stack.get()          # 8
second_last = stack.get()   # 9
print('Sum of the last two numbers:', last + second_last)

# Suma pozostałych elementów stosu. Pętla while działa, dopóki stos nie jest pusty.
remaining_sum = 0
while not stack.empty():
    remaining_sum += stack.get()
print('Sum of the remaining stack elements:', remaining_sum)
