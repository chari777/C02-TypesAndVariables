###
# Oblicza, wypisuje i zapisuje do pliku liczby 1..100 oraz ich kwadraty i sześciany
#
output_file = 'powers.txt'

with open(output_file, 'w', encoding='utf-8') as file:
    for n in range(1, 101):
        # Zapis w formacie: liczba,kwadrat,sześcian
        line = f'{n},{n ** 2},{n ** 3}'
        print(line)
        file.write(line + '\n')
