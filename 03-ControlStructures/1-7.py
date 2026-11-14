basic_salary = 5000
total_salary = 0
bonus = 0.30 # 30% (w zadaniu kazali sprawdzić dla 30%, w kodzie wzorcowym było 0.15)

# porównanie == 'Y' od razu zwraca True albo False i zapisuje to do zmiennej is_bonus
is_bonus = input('Does the employee receive a bonus? (Y/N): ') == 'Y'

if is_bonus:
    total_salary = basic_salary + (basic_salary * bonus) # dodaję premię do podstawy
else:
    total_salary = basic_salary # bez premii dostaję samą podstawę

print(f'Basic salary: {basic_salary}')
print(f'Bonus included? {is_bonus}')
print(f'Total salary: {total_salary}')