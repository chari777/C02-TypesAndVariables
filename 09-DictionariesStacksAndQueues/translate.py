###
# Tłumacz angielsko-polski: użytkownik wpisuje słowo po angielsku,
# program pokazuje tłumaczenie albo informację, że go nie ma w słowniku.
#
translations = {
    'computer': 'komputer',
    'mouse': 'myszka',
    'keyboard': 'klawiatura',
    'printer': 'drukarka'
}

word = input('Enter an English word: ').strip().lower()

# 'in' sprawdza, czy klucz istnieje w słowniku - zanim odczytamy wartość
if word in translations:
    print(f'{word} -> {translations[word]}')
else:
    print('Sorry, the translation is unavailable.')
