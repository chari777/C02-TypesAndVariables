###
# Zapisuje ulubioną książkę (słownik z pięcioma parami) do pliku favourite.json
#
import json

favourite_book = {
    "title": "The Hobbit",
    "author": "J.R.R. Tolkien",
    "year": 1937,
    "genre": "Fantasy",
    "rating": 9.5
}

with open('favourite.json', 'w', encoding='utf-8') as file:
    json.dump(favourite_book, file, indent=4, ensure_ascii=False)

print('Favourite book saved to favourite.json')
