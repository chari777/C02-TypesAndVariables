###
# Wyświetla po pięć pierwszych linii pliku it_company.csv.
# Po każdej porcji czeka na naciśnięcie Enter, a potem pokazuje kolejne pięć linii.
#
with open('it_company.csv', 'r', encoding='utf-8') as file:
    lines = file.read().splitlines()

PAGE_SIZE = 5   # ile linii pokazujemy naraz
start = 0
# Pętla działa, dopóki nie wyświetlimy wszystkich linii
while start < len(lines):
    # Wypisujemy porcję od 'start' do 'start + PAGE_SIZE' (ostatnia może być krótsza)
    for line in lines[start:start + PAGE_SIZE]:
        print(line)
    start += PAGE_SIZE
    # Czekamy na Enter tylko wtedy, gdy zostały jeszcze linie do pokazania
    if start < len(lines):
        # print() wypisuje komunikat w osobnej linii, a input() czeka na Enter
        print('Press Enter key...')
        input()
