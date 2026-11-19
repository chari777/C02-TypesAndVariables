###
# Moduł z funkcją zwracającą nazwę miesiąca na podstawie jego numeru
#
def month(n):
    # Lista nazw; indeks 0 odpowiada styczniowi, więc numer miesiąca minus 1
    months_names = ['January', 'February', 'March', 'April', 'May', 'June',
                    'July', 'August', 'September', 'October', 'November', 'December']
    # Sprawdzamy zakres 1..12, żeby nie wyjść poza listę
    if 1 <= n <= 12:
        return months_names[n - 1]
    return ''
