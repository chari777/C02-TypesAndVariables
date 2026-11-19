# KROKI RYSOWANIA:
# 1. penup() - pisak podniesiony, żółw może się ruszać bez rysowania.
# 2. goto(x, y) - przesunięcie na współrzędne (0,0 = środek ekranu).
# 3. pendown() - pisak opuszczony, znowu rysujemy.
# 4. Wywołujemy funkcję rysującą figurę z modułu figures.py.
###
# Rysuje każdą figurę (kwadrat, trójkąt, prostokąt) dwa razy,
# w różnych miejscach ekranu.
#
import turtle
import figures

window = turtle.Screen()
window.bgcolor("lightgreen")
turtle.speed(5)

# --- Kwadrat ---
# Pierwszy kwadrat rysujemy od punktu startowego (środek ekranu)
figures.draw_square(100)

# penup() podnosi pisak, żeby żółw mógł się przesunąć bez rysowania.
# goto(x, y) przenosi żółwia na współrzędne ekranu (0,0 to środek).
turtle.penup()
turtle.goto(-200, 150)
# pendown() opuszcza pisak, żeby kolejne ruchy znowu rysowały.
turtle.pendown()
figures.draw_square(60)

# --- Trójkąt ---
turtle.penup()
turtle.goto(100, -150)
turtle.pendown()
figures.draw_triangle(120)

turtle.penup()
turtle.goto(-250, -150)
turtle.pendown()
figures.draw_triangle(80)

# --- Prostokąt ---
turtle.penup()
turtle.goto(50, 200)
turtle.pendown()
figures.draw_rectangle(120, 60)

turtle.penup()
turtle.goto(-200, -50)
turtle.pendown()
figures.draw_rectangle(60, 40)

turtle.hideturtle()
window.mainloop()
