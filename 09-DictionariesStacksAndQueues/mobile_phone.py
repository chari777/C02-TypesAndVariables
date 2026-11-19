###
# Słownik opisujący mój telefon komórkowy (6 par klucz-wartość).
# Pętla for z items() daje dostęp jednocześnie do klucza i wartości.
#
mobile = {
    "OS": "Android",
    "brand": "Samsung",
    "model": "Galaxy A54",
    "storage_GB": 128,
    "color": "Black",
    "year": 2023
}

for key, value in mobile.items():
    print(f"{key} : {value}")
