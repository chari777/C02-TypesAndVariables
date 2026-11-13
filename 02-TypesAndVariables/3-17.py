import math

# input() zawsze wczytuje tekst, więc muszę owinąć go w float(), żeby mieć liczbę z ułamkiem (np. 1.8)
h = float(input("Enter observer height in meters: "))

d = 3.57 * math.sqrt(h) # podstawiam wysokość pod wzór z zadania (3.57 razy pierwiastek z h)

print("Distance to the horizon in km:", round(d, 2))