###
# Łączy dwa słowniki z danymi osobowymi w jeden słownik 'person'
#
basic_data = {
    "name": "Barbara",
    "age": 21
}

advanced_data = {
    "status": "student",
    "married": False,
    "interest": ["reading", "swimming"]
}

# Operator ** rozpakowuje pary klucz-wartość z obu słowników do nowego słownika
person = {**basic_data, **advanced_data}
print('Person:', person)
