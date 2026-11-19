###
# Operacje na słowniku 'person' - odczyt, zmiana, dodawanie i usuwanie danych.
#
person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming", "excursions"],
    "married": True,
    "phone": {"landline": "123444321", "mobile": "777888999"}
}

# Typy wartości w słowniku: napis (str), liczba (int), lista (list),
# wartość logiczna (bool) i kolejny słownik (dict).

# 1. Wypisanie imienia - odczyt wartości po kluczu w nawiasach []
print('Name:', person['name'])
# 2. Wypisanie hobby (lista)
print('Hobby:', person['hobby'])
# 3. Wypisanie całego słownika
print('Full dictionary:', person)
# 4. Zmiana nazwiska - przypisanie do istniejącego klucza nadpisuje wartość
person['surname'] = 'Nowak'
# 5. Zmiana stanu cywilnego na przeciwny. 'not' odwraca True/False.
person['married'] = not person['married']
# 6. Dodanie nowego klucza 'gender' - przypisanie do nieistniejącego klucza go tworzy
person['gender'] = 'male'
# 7. Nowe hobby dodajemy do listy, nie do słownika
person['hobby'].append('bicycle')
# 8. Telefon służbowy - słownik zagnieżdżony, dodajemy nowy klucz wewnątrz 'phone'
person['phone']['work'] = '313131444'
# 9. Wypisanie całego słownika pętlą po parach klucz-wartość
print('Person data:')
for key, value in person.items():
    print(f'{key} : {value}')
