###
# Zwraca nazwę dnia tygodnia dla podanego numeru (1-poniedziałek ... 7-niedziela)
#
def weekday(n):
    weekdays = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]
    # Numer dnia zaczyna się od 1, a indeks listy od 0, więc odejmujemy 1
    return weekdays[n - 1]

# Wypisujemy nazwy dla numerów 1, 4 i 7
print(weekday(1))
print(weekday(4))
print(weekday(7))
