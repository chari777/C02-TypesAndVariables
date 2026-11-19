###
# Sumuje liczbę zaparkowanych samochodów z ostatnich pięciu dni (plik car_park.txt)
#
def read_from_file(name):
    with open(name, encoding='utf-8') as file:
        content = file.read()
    return content

# Czytamy cały plik i dzielimy na linie - każda linia to jeden dzień
file_content = read_from_file('car_park.txt')
file_lines = file_content.splitlines()

total = 0
for line in file_lines:
    # Każda linia to tekst, np. '25'. int() zamienia go na liczbę do dodawania.
    total += int(line)

print('Total cars parked:', total)
