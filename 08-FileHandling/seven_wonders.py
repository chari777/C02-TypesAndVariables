###
# Zapisuje Siedem Cudów Świata do pliku, każde w osobnej linii, alfabetycznie
#
seven_wonders = [
    "Great Wall of China",
    "Petra",
    "Christ the Redeemer",
    "Machu Picchu",
    "Chichen Itza",
    "Roman Colosseum",
    "Taj Mahal"
]

file_name = 'seven_wonders.txt'

# sorted() zwraca posortowaną kopię listy, oryginał zostaje bez zmian
sorted_wonders = sorted(seven_wonders)

with open(file_name, 'w', encoding='utf-8') as file:
    for item in sorted_wonders:
        # Każdy napis zapisujemy z \n na końcu, żeby kolejny był w nowej linii
        file.write(item + '\n')

print(f'Seven wonders have been written to {file_name}.')
