# Moduł z funkcjami do zamiany jednostek długości.
# Ten plik można importować w innych programach (import converters).

# Zamiana metrów na centymetry: 1 m = 100 cm
def m_to_cm(n):
    return n*100

# Zamiana centymetrów na metry: 1 cm = 0.01 m
def cm_to_m(n):
    return n/100

# Zamiana centymetrów na cale (inches). 1 cal = 2.54 cm
def cm_to_inch(n):
    return n/2.54

# Zamiana stóp i cali na centymetry.
# Najpierw zamieniamy stopy na cale (1 stopa = 12 cali), dodajemy cale,
# a na końcu całość mnożymy przez 2.54, żeby dostać centymetry.
def feet_inches_to_cm(feet, inches):
    total_inches = feet*12 + inches
    return total_inches*2.54

if __name__ == "__main__":
    # Ten blok uruchamia się tylko przy bezpośrednim uruchomieniu tego pliku
    # (nie przy imporcie), dzięki temu możemy tu przetestować funkcje
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
    print(f'254cm = {cm_to_inch(254)} inches')
    print(f"5 feet 7 inches = {feet_inches_to_cm(5, 7):.1f}cm")
