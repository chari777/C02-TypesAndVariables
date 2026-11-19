###
# Wypisuje gry komputerowe posortowane alfabetycznie i ponumerowane.
# Używamy pętli while (zgodnie z zadaniem).
#
computer_games = [
    "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
    "League of Legends", "Valorant", "Grand Theft Auto V",
    "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]

# sorted() zwraca NOWĄ, posortowaną listę. Oryginał zostaje bez zmian.
sorted_games = sorted(computer_games)

# Pętla while działa, dopóki indeks jest mniejszy od liczby elementów.
# Indeks i zaczyna od 0 i musimy go ręcznie zwiększać, inaczej pętla nie skończy się nigdy.
i = 0
while i < len(sorted_games):
    # Numerujemy od 1, więc wypisujemy i+1
    print(f"{i + 1}. {sorted_games[i]}")
    i += 1
