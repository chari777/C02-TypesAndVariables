movie = "The Batman: The Dark Knight"

print('Number of characters: ', len(movie))
print('Capital letters: ', movie.upper()) # zamieniam cały tekst na WIELKIE LITERY
print('Small letters: ', movie.lower())   # zamieniam cały tekst na małe litery
print('Count of "e": ', movie.count('e')) # liczę ile razy pojawia się mała litera 'e'
print('Position of "Batman": ', movie.find('Batman'))     # szukam na którym indeksie zaczyna się słowo 'Batman'
print('Position of "rises": ', movie.find('rises')) # zwraca -1, co oznacza, że takiego słowa tu nie ma