###
# Tygodniowy plan posiłków: śniadanie, obiad, kolacja
#
meal_plan = [
    ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
    ["Pancakes", "Sandwich", "Steak"],
    ["Smoothie", "Chicken Wrap", "Salmon"],
    ["Eggs", "Pasta", "Soup"],
    ["Toast", "Burrito", "Pizza"],
    ["Cereal", "Salad", "Fish Tacos"],
    ["Bagel", "Rice and Beans", "Stir-fry"]
]

# Zwraca nazwę dnia (1 = Monday ... 7 = Sunday)
def weekday(n):
    weekdays = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[n - 1]

# Zwraca posiłki z danego dnia jako napis oddzielony przecinkami
def day_meal_plan(meal_plan, day_number):
    # Numer dnia minus 1 to indeks wiersza w liście
    return ", ".join(meal_plan[day_number - 1])

print('WEEKLY MEAL PLAN')
print('(Breakfast, Lunch, Dinner)')
print('==========================')
for day in range(1, 8):
    print(f'{weekday(day)}: {day_meal_plan(meal_plan, day)}')
