# KROKI (kwadrat): 4 razy: idź naprzód o bok, obróć w prawo o 90 stopni.
# KROKI (prostokąt): bok a, obrót, bok b, obrót, bok a, obrót, bok b, obrót.
# KROKI (trójkąt): zewnętrzny kąt zakrętu = 180 - kąt wewnętrzny.
#   Kąty przy podstawie 70, przy wierzchołku 40 -> zakręty 110, 140, 110 (suma 360).
#   Suma zakrętów 360 stopni oznacza, że figura się zamyka.
###
# Moduł z funkcjami rysującymi figury żółwiem (moduł turtle).
#
# Funkcje używają domyślnego żółwia, więc nie trzeba przekazywać
# obiektu pen. Wystarczy wywołać np. draw_square(100).
import turtle

# Rysuje kwadrat o boku 'length'
def draw_square(length):
    # Cztery razy: idź do przodu i obróć o 90 stopni w prawo.
    # Po czterech obrotach żółw wraca do punktu startowego i w tym samym kierunku.
    for i in range(4):
        turtle.forward(length)
        turtle.right(90)

# Rysuje trójkąt równoramienny.
# Podstawa ma długość 'length'. Kąt przy wierzchołku wynosi 40 stopni,
# a ramiona liczymy z twierdzenia o sinusach, żeby trójkąt był zamknięty.
def draw_triangle(length):
    apex_angle = 40
    # Długość ramienia: podstawa / (2 * sin(kąt przy wierzchołku / 2))
    import math
    leg = length / (2 * math.sin(math.radians(apex_angle / 2)))
    # Kąty przy podstawie: (180 - 40) / 2 = 70 stopni.
    # Obrót w lewo o 180 - kąt wewnętrzny daje zewnętrzny kąt zakrętu.
    turtle.forward(length)        # podstawa
    turtle.left(180 - 70)         # skręt w rogu podstawy
    turtle.forward(leg)           # pierwsze ramię
    turtle.left(180 - apex_angle) # skręt przy wierzchołku
    turtle.forward(leg)           # drugie ramię
    turtle.left(180 - 70)         # powrót do kierunku startowego

# Rysuje prostokąt o bokach a i b
def draw_rectangle(length_a, length_b):
    # Dwa boki o długości a i dwa o długości b, z obrotami o 90 stopni
    turtle.forward(length_a)
    turtle.left(90)
    turtle.forward(length_b)
    turtle.left(90)
    turtle.forward(length_a)
    turtle.left(90)
    turtle.forward(length_b)
    turtle.left(90)
