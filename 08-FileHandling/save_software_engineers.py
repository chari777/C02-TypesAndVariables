###
# Zapisuje pracowników na stanowisku 'Software Engineer' do pliku software_engineer.txt
#

# Nazwy plików i stanowisko
employees_file = 'it_company.csv'
position_file = 'software_engineer.txt'
job_title = 'Software Engineer'

# Dwa bloki with: jeden do odczytu, drugi do zapisu.
# Nie trzeba ich zamykać ręcznie - zrobi to Python.
with open(employees_file, 'r', encoding='utf-8') as source:
    with open(position_file, 'w', encoding='utf-8') as target:
        for line in source:
            # Zapisujemy tylko linie zawierające stanowisko
            if job_title in line:
                target.write(line)

print(f'Employees saved to {position_file}.')
