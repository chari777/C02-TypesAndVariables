# Program testowy - używa funkcji z modułu converters
# import converters szuka pliku converters.py w tym samym folderze
import converters

print('### Test converters')
print(f'Three meters is {converters.m_to_cm(3)}cm')
print(f'250cm is {converters.cm_to_m(250)}m')
# Wynik w calach zaokrąglamy do 2 miejsc po przecinku, żeby był czytelny
print(f'100cm is {converters.cm_to_inch(100):.2f} inches')
# Zamiana 6 stóp i 0 cali na centymetry
print(f'6 feet 0 inches is {converters.feet_inches_to_cm(6, 0):.2f}cm')
