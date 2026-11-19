###
# Wczytuje i wypisuje dane pracownika.
# Ze względu na ochronę danych osobowych użytkownik decyduje,
# czy wynagrodzenie zostanie wypisane.
#
# Importujemy nasz własny moduł keyboard.py z tego samego folderu.
# Ponieważ importujemy cały moduł, funkcje wołamy z prefiksem keyboard.
import keyboard

# Wczytujemy dane pracownika z klawiatury.
# Każda funkcja zwraca wartość już w odpowiednim typie.
first_name = keyboard.input_string('Enter name: ')
last_name = keyboard.input_string('Enter last name: ')
age = keyboard.input_integer('Enter age: ')
salary = keyboard.input_real('Enter salary: ')
is_salary_hidden = keyboard.input_boolean('Hide salary? (y/n) ')

# Wypisujemy kartę pracownika
print('DATA RECORD')
print('===========')
print('Name:', first_name)
print('Last name:', last_name)
print('Age:', age)
# Wynagrodzenie pokazujemy tylko wtedy, gdy użytkownik NIE chciał je ukryć.
# "not" odwraca wartość: jeśli is_salary_hidden to False, warunek jest prawdziwy.
if not is_salary_hidden:
    print('Salary:', salary)
