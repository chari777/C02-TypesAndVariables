###
# Sumuje godziny wszystkich przedmiotów w semestrze zimowym
#
winter_semester = {
    "math": 60,
    "programming": 30,
    "history": 15
}

# sum() dodaje wszystkie wartości słownika (tu: liczby godzin)
total_hours = sum(winter_semester.values())
print(f'The total number of hours in the winter semester is {total_hours}')
