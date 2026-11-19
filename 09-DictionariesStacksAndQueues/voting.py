# KROKI:
# 1. Jeśli voting.json istnieje - wczytujemy słownik {imię: liczba głosów}.
# 2. Jeśli nie - zaczynamy od pustego słownika {}.
# 3. votes.get(imię, 0) + 1 - nowa osoba ma 0 i dostaje 1, znana dostaje o jeden więcej.
# 4. Zapisujemy cały słownik z powrotem do pliku (json.dump).
###
# System głosowania: wyniki zapisywane są w pliku voting.json.
# Każde uruchomienie programu dodaje jeden głos dla wpisanej osoby.
#
import json
import os

VOTING_FILE = 'voting.json'

# Odczyt dotychczasowych wyników. Jeśli plik jeszcze nie istnieje, zaczynamy od pustego słownika.
if os.path.exists(VOTING_FILE):
    with open(VOTING_FILE, 'r', encoding='utf-8') as file:
        votes = json.load(file)
else:
    votes = {}

person_name = input('Name of the person you are voting for: ').strip()

# get(name, 0) zwraca liczbę głosów lub 0 dla nowej osoby, a potem dodajemy 1
votes[person_name] = votes.get(person_name, 0) + 1

# Zapis całego słownika z powrotem do pliku (indent=4 dla czytelności)
with open(VOTING_FILE, 'w', encoding='utf-8') as file:
    json.dump(votes, file, indent=4, ensure_ascii=False)

print(f'Thank you! {person_name} now has {votes[person_name]} vote(s).')
