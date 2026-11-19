###
# Rysuje kwadrat żółwiem. Funkcję draw_square bierzemy z modułu figures.py
#
import turtle
import figures

# Ustawienie okna
window = turtle.Screen()
window.bgcolor("lightgreen")

# Ustawienie żółwia
turtle.speed(5)

# Narysuj kwadrat o boku 100 pikseli
figures.draw_square(100)

# Ukryj żółwia i czekaj, aż okno zostanie zamknięte przez użytkownika.
# mainloop() trzyma okno otwarte; bez niego okno zamknęłoby się od razu.
turtle.hideturtle()
window.mainloop()
