# JAK CZYTAĆ TEN PLIK:
# Każda funkcja ma swoje wyjaśnienie w komentarzu nad nią.
# Na dole (blok if __name__ == "__main__") są testy assert - jeśli program
# dojdzie do końca i wypisze 'All practice function tests passed', to wszystkie
# przykłady z zadania się zgadzają.
###
# Zbiór funkcji z sekcji "Practice Makes Perfect".
# Każda funkcja ma przykłady z zadania. Na dole pliku są testy (assert),
# które sprawdzają, czy wyniki zgadzają się z przykładami.
#

# Sprawdza, czy napis jest poprawną liczbą binarną (same znaki '0' i '1')
def is_binary(binary_number):
    # Pusty napis nie jest liczbą, więc odrzucamy go od razu
    if binary_number == '':
        return False
    # all() zwraca True, jeśli WSZYSTKIE elementy spełniają warunek
    for char in binary_number:
        if char not in '01':
            return False
    return True

# Zwraca minimalną liczbę monet 1, 2 i 5 zł potrzebnych do zapłaty.
# Zachłanne podejście: zawsze bierzemy największą możliwą monetę.
# Dla tych nominałów takie podejście daje wynik minimalny.
def min_coins(amount_to_pay):
    coins = [5, 2, 1]
    count = 0
    for coin in coins:
        # Dzielenie całkowite // mówi, ile razy moneta mieści się w kwocie
        count += amount_to_pay // coin
        # Reszta z dzielenia % to kwota, którą trzeba zapłacić mniejszymi monetami
        amount_to_pay = amount_to_pay % coin
    return count

# Sumuje parzyste (even=True) lub nieparzyste (even=False) cyfry liczby
def sum_even_odd_digits(number, even):
    total = 0
    for char in str(abs(number)):
        digit = int(char)
        # digit % 2 == 0 oznacza, że cyfra jest parzysta
        if (digit % 2 == 0) == even:
            total += digit
    return total

# Liczy ujemne liczby parzyste w przedziale <x, y>
def count_negative_even(x, y):
    count = 0
    for n in range(x, y + 1):    # +1, bo range nie obejmuje końca
        # Ujemna: n < 0. Parzysta: reszta z dzielenia przez 2 równa 0.
        if n < 0 and n % 2 == 0:
            count += 1
    return count

# True, jeśli którakolwiek z trzech liczb jest ujemna
def any_negative(n1, n2, n3):
    # any() zwraca True, jeśli choć jeden element listy jest True
    return any(n < 0 for n in [n1, n2, n3])

# Zwraca napis z n gwiazdkami oddzielonymi ukośnikiem
def asterisks(n):
    # '/'.join(...) skleja elementy listy, wstawiając '/' między nimi
    return '/'.join('*' * 1 for _ in range(n))

# Zwraca liczby od 1 do n jako jeden długi napis
def numbers_to_string(n):
    result = ''
    for i in range(1, n + 1):
        result += str(i)
    return result

# Wykonuje działanie na dwóch liczbach według podanego operatora
def calculate(number1, number2, operator):
    # Dla każdego operatora osobny warunek. Zwracamy wynik od razu.
    if operator == '+':
        return number1 + number2
    if operator == '-':
        return number1 - number2
    if operator == '*':
        return number1 * number2
    if operator == '%':
        return number1 % number2
    if operator == '**':
        return number1 ** number2
    return None

# Urządzenie w drzwiach: '+' to wejście, '-' to wyjście.
# Zwraca True, jeśli w pewnym momencie w pokoju było co najmniej 3 osoby.
def too_crowded(detector):
    people_inside = 0
    for event in detector:
        if event == '+':
            people_inside += 1
        elif event == '-':
            people_inside -= 1
        # Sprawdzamy po każdym zdarzeniu, czy próg 3 osób został osiągnięty
        if people_inside >= 3:
            return True
    return False

# n-ta liczba Fibonacciego. Ciąg: 0, 1, 1, 2, 3, 5, ... (numeracja od 1)
def fibonacci(n):
    # a i b to dwie kolejne wartości ciągu. Na starcie a = 0 (1. wyraz), b = 1 (2. wyraz)
    a, b = 0, 1
    # Po n-1 krokach a wskazuje na n-ty wyraz
    for _ in range(n - 1):
        # Równoległe przypisanie: nowe a = stare b, nowe b = suma obu
        a, b = b, a + b
    return a

# True, jeśli napis czytany od tyłu wygląda identycznie
def is_palindrome(palindrome):
    # text[::-1] to napis odwrócony (krok -1 idzie od końca)
    return palindrome == palindrome[::-1]

# Usuwa wszystkie spacje z napisu
def remove_spaces(sentence):
    # replace() zamienia każde wystąpienie ' ' na pusty napis
    return sentence.replace(' ', '')

# Suma cyfr, które w liczbie występują więcej niż jeden raz (każde wystąpienie)
def sum_repeated_digits(number):
    digits = str(abs(number))
    total = 0
    for char in digits:
        # count() zlicza wystąpienia tej cyfry w całym napisie
        if digits.count(char) > 1:
            total += int(char)
    return total

# Zwraca n-tą liczbę pierwszą (numeracja od 1: 2, 3, 5, 7, 11, ...)
def nth_prime(n):
    # Sprawdza, czy liczba jest pierwsza: dzielimy tylko przez liczby do pierwiastka
    def is_prime(num):
        if num < 2:
            return False
        divisor = 2
        while divisor * divisor <= num:
            if num % divisor == 0:
                return False
            divisor += 1
        return True

    count = 0
    candidate = 1
    # Szukamy kolejnych liczb pierwszych, aż znajdziemy n-tą
    while count < n:
        candidate += 1
        if is_prime(candidate):
            count += 1
    return candidate

# Różnica między największą a najmniejszą z trzech liczb
def max_min_difference(number1, number2, number3):
    return max(number1, number2, number3) - min(number1, number2, number3)

# Akronim: pierwsze litery wszystkich słów, zachowując wielkość liter
def acronym(name):
    # split() dzieli napis na słowa po spacjach
    # w każdym słowie bierzemy pierwszą literę [0]
    return ''.join(word[0] for word in name.split())

# Hasło jest poprawne, gdy ma co najmniej 6 znaków i każdy znak występuje tylko raz
def is_valid_password(password):
    if len(password) < 6:
        return False
    # set() usuwa powtórzenia. Jeśli długość zbioru jest równa długości hasła,
    # to wszystkie znaki były różne.
    return len(set(password)) == len(password)

# Oblicza wartość wyrażenia z jednocyfrowymi liczbami, '+' i '-'
def evaluate_expression(expression):
    result = 0
    # Znak przed kolejną liczbą: +1 lub -1. Domyślnie plus.
    sign = 1
    for char in expression:
        if char == '+':
            sign = 1
        elif char == '-':
            sign = -1
        elif char.isdigit():
            # Dodajemy liczbę ze znakiem przed nią
            result += sign * int(char)
    return result

# Suma liczb z przedziału <x, y>, które dzielą się przez 2 i 3, a NIE dzielą się przez 4.
# Podzielne przez 2 i 3 jednocześnie = podzielne przez 6.
def sum_divisible_by_6_not_4(x, y):
    total = 0
    for n in range(x, y + 1):
        if n % 6 == 0 and n % 4 != 0:
            total += n
    return total

# Wstawia myślnik między wszystkie znaki tekstu
def dash_separated(text):
    # '-'.join(text) łączy kolejne znaki (napis to ciąg znaków)
    return '-'.join(text)

# Sprawdza poprawność 4-cyfrowego kodu produktu.
# Czwarta cyfra = reszta z dzielenia sumy trzech pierwszych cyfr przez 7.
def is_valid_product_code(product_code):
    # Kod musi mieć dokładnie 4 znaki i wszystkie muszą być cyframi
    if len(product_code) != 4 or not product_code.isdigit():
        return False
    control = sum(int(c) for c in product_code[:3]) % 7
    return int(product_code[3]) == control

# Zwraca wartość oczka, które wypadło najwięcej razy z rzędu (najdłuższa seria)
def longest_run_value(dice):
    best_value = ''
    best_length = 0
    current_length = 0
    previous = ''
    for roll in dice:
        # Jeśli wynik jest taki sam jak poprzedni, seria rośnie
        if roll == previous:
            current_length += 1
        else:
            # Nowa seria zaczyna się od 1
            current_length = 1
        # Zapamiętujemy serię tylko wtedy, gdy jest dłuższa niż dotychczasowa najdłuższa
        if current_length > best_length:
            best_length = current_length
            best_value = roll
        previous = roll
    # Zwracamy liczbę (int), a nie napis
    return int(best_value)

# Testy - każdy assert sprawdza jeden przykład z zadania
if __name__ == "__main__":
    assert is_binary("101101") is True
    assert is_binary("1311a10100") is False

    assert min_coins(23) == 6
    assert min_coins(8) == 3
    assert min_coins(2) == 1
    assert min_coins(0) == 0

    assert sum_even_odd_digits(3124, True) == 6
    assert sum_even_odd_digits(3124, False) == 4
    assert sum_even_odd_digits(20576, False) == 12
    assert sum_even_odd_digits(20576, True) == 8
    assert sum_even_odd_digits(13115, True) == 0

    assert count_negative_even(-7, 8) == 3
    assert count_negative_even(-1, 11) == 0

    assert any_negative(11, 6, -4) is True
    assert any_negative(5, 4, 14) is False

    assert asterisks(4) == "*/*/*/*"
    assert asterisks(1) == "*"

    assert numbers_to_string(11) == "1234567891011"
    assert numbers_to_string(4) == "1234"

    assert calculate(2, 3, "+") == 5
    assert calculate(2, 3, "%") == 2
    assert calculate(2, 3, "**") == 8
    assert calculate(2, 3, "*") == 6
    assert calculate(2, 3, "-") == -1

    assert too_crowded("+-+++-+---") is True
    assert too_crowded("+-+-+-+-") is False
    assert too_crowded("+-++-+--") is False
    assert too_crowded("+-++-++-+---") is True

    assert fibonacci(5) == 3
    assert fibonacci(9) == 21

    assert is_palindrome("radar") is True
    assert is_palindrome("12-11-21") is True
    assert is_palindrome("book") is False

    assert remove_spaces("integrated development environment") == "integrateddevelopmentenvironment"
    assert remove_spaces("A programming language is a system of notation for writing computer programs") == \
        "Aprogramminglanguageisasystemofnotationforwritingcomputerprograms"

    assert sum_repeated_digits(1027) == 0
    assert sum_repeated_digits(230335) == 9
    assert sum_repeated_digits(513553007) == 21

    assert nth_prime(1) == 2
    assert nth_prime(5) == 11

    assert max_min_difference(7, 4, 9) == 5
    assert max_min_difference(2, 12, 8) == 10

    assert acronym("Internet of Things") == "IoT"
    assert acronym("For Your Information") == "FYI"
    assert acronym("Python") == "P"

    assert is_valid_password("ax15") is False
    assert is_valid_password("book123") is False
    assert is_valid_password("A2water3") is True
    assert is_valid_password("qwerty") is True
    assert is_valid_password("") is False

    assert evaluate_expression("2+3") == 5
    assert evaluate_expression("3+8+1") == 12
    assert evaluate_expression("2+3-4+5-0") == 6

    assert sum_divisible_by_6_not_4(1, 20) == 24
    assert sum_divisible_by_6_not_4(10, 30) == 48

    # W zadaniu przykład ma literówkę: dla wejścia "Univesity" (bez "r")
    # poprawny wynik to "U-n-i-v-e-s-i-t-y". Test sprawdza wersję zgodną z wejściem.
    assert dash_separated("Univesity") == "U-n-i-v-e-s-i-t-y"
    assert dash_separated("UE") == "U-E"
    assert dash_separated("x") == "x"
    assert dash_separated("") == ""

    assert is_valid_product_code("1082") is True
    assert is_valid_product_code("2035") is True
    assert is_valid_product_code("1114") is False
    assert is_valid_product_code("7071") is False

    assert longest_run_value("5233165554211") == 5
    assert longest_run_value("2133") == 3

    print('All practice function tests passed.')
