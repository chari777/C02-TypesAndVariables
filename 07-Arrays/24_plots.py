###
# Wykresy w matplotlib: linia, parabola i sinus.
#
# Najpierw instalujemy bibliotekę: pip install matplotlib
import math
import matplotlib.pyplot as plt

# --- Linia od punktu (1, 3) do punktu (8, 10) ---
xpoints = [1, 8]
ypoints = [3, 10]
plt.figure()
plt.plot(xpoints, ypoints)
plt.title('Line from (1,3) to (8,10)')
plt.show()

# --- f(x) = x^2 - 3 ---
# Tworzymy listę x: liczby od -100 do 100 włącznie
x = []
for n in range(-100, 101):
    x = x + [n]
# Dla każdego x liczymy y = x^2 - 3
y = []
for n in x:
    y.append(n ** 2 - 3)
plt.figure()
plt.plot(x, y)
plt.title('f(x) = x^2 - 3')
plt.show()

# --- y = sin(x) dla kąta od 0 do 360 stopni ---
angles = list(range(0, 361))
# math.sin przyjmuje radiany, więc stopnie zamieniamy funkcją radians()
sines = [math.sin(math.radians(a)) for a in angles]
plt.figure()
plt.plot(angles, sines)
plt.title('y = sin(x), 0-360 degrees')
plt.show()
