###
# Wydatki miesięczne podzielone na kategorie (kolumny) i tygodnie (wiersze)
#
# Kolumny: [Food, Transport, Utilities]
monthly_expenses = [
    [200, 50, 100],   # Week 1
    [180, 60, 110],   # Week 2
    [220, 55, 105],   # Week 3
    [210, 65, 95]     # Week 4
]

# Liczba kategorii to długość pierwszego wiersza
categories_count = len(monthly_expenses[0])

# Sumy dla kategorii: dla każdej kolumny sumujemy wartości ze wszystkich wierszy
category_totals = [0] * categories_count
for week in monthly_expenses:
    for c in range(categories_count):
        category_totals[c] += week[c]

# Sumy dla tygodni: dla każdego wiersza sumujemy wszystkie wartości w nim
week_totals = []
for week in monthly_expenses:
    week_sum = 0
    for value in week:
        week_sum += value
    week_totals.append(week_sum)

# Suma miesięczna to suma wszystkich wydatków (lub suma sum tygodni)
month_total = sum(week_totals)

print('MONTHLY EXPENSES')
print('----------------')
print('Food:', category_totals[0])
print('Transport:', category_totals[1])
print('Utilities:', category_totals[2])
for i in range(len(week_totals)):
    print(f'Week {i + 1}:', week_totals[i])
print('---------------')
print('TOTAL:', month_total)
