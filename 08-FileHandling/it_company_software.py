###
# Wypisuje pracowników zatrudnionych na stanowisku 'Software Engineer'.
# Dane są w pliku it_company.csv (w zadaniu błędnie podano .txt).
#
file_name = 'it_company.csv'
job_title = 'Software Engineer'

# with ... as ... - plik zostanie zamknięty automatycznie po wyjściu z bloku
with open(file_name, 'r', encoding='utf-8') as file:
    counter = 1
    # Pierwsza linia to nagłówek - pomijamy ją, bo nie jest danymi pracownika
    next(file)
    for line in file:
        # 'in' sprawdza, czy tekst stanowiska znajduje się w linii
        if job_title in line:
            # strip() usuwa znak nowej linii z końca, żeby print nie robił pustej linii
            print(f'{counter}. {line.strip()}')
            counter += 1
