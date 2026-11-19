# KROKI (przycisk Wstecz):
# 1. Nowa strona: poprzednia strona bieżąca idzie na STOS (put), nowa staje się bieżącą.
# 2. Wpisane 0: zdejmujemy ze stosu (get) ostatnią stronę i ustawiamy jako bieżącą.
# 3. Stos pusty przy 0 -> nie ma dokąd wrócić, kończymy program (break).
# Dlaczego stos? Ostatnio odwiedzona strona musi być pierwsza do powrotu - to LIFO.
###
# Symulacja przycisku "Wstecz" w przeglądarce.
# Historia odwiedzonych stron to stos (LIFO): ostatnio odwiedzona strona jest na wierzchu.
#
import queue

# Stos historii z wcześniej odwiedzonymi stronami
visited_websites = queue.LifoQueue()

# Poprzednio odwiedzone strony (microsoft.com jest na samym wierzchu)
visited_websites.put('instagram.com')
visited_websites.put('uek.krakow.pl')
visited_websites.put('microsoft.com')

# Aktualnie oglądana strona. Na początku jeszcze żadnej nie ma.
current_website = ''

while True:
    website = input('Enter website name (0 for back): ')

    if website == '0':
        # Przycisk "Wstecz". Jeśli historia jest pusta, nie ma dokąd wrócić - kończymy.
        if visited_websites.empty():
            break
        print('<-- Going back to a previously visited website')
        # Zdejmujemy ze stosu poprzednią stronę i ustawiamy ją jako bieżącą
        current_website = visited_websites.get()
    elif website != '':
        # Nowa strona: poprzednią bieżącą odkładamy na stos, żeby można było do niej wrócić
        if current_website != '':
            visited_websites.put(current_website)
        current_website = website

    # Wypisujemy nazwę strony, którą aktualnie "oglądamy"
    print('You are currently viewing:', current_website)
    print()
