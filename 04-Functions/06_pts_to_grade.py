# KROKI:
# 1. Sprawdzamy progi od NAJWYŻSZEGO (18) do najniższego (10).
# 2. Pierwszy spełniony warunek ustawia ocenę - reszta elif/else jest pomijana.
# 3. Jeśli żaden warunek nie pasuje (poniżej 10), wpada w else -> 'Fail'.
# 4. Funkcja zwraca napis z oceną, a program go wypisuje.
###
# Zwraca ocenę końcową z testu na podstawie liczby zdobytych punktów
#
# Funkcja sprawdza progi od najwyższego do najniższego.
# Dlaczego od najwyższego? Bo wtedy wystarczy sprawdzić jeden warunek,
# a nie trzeba pilnować zakresów dla każdej oceny.
def pts_to_grade(points):
    grade = ''
    if points >= 18:
        grade = 'Excellent'
    elif points >= 14:
        grade = 'Good'
    elif points >= 10:
        grade = 'Satisfactory'
    else:
        grade = 'Fail'
    return grade

test_result = 15
final_grade = pts_to_grade(test_result)
print(f'You scored {test_result} points on the test. Your final grade is {final_grade}')
