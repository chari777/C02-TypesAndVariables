###
# Statystyki wyniku testu. True = poprawna odpowiedź, False = błędna.
#
test_results = [
    False, True, False, True, True,
    True, True, False, True, True,
    False, True, True, True, False
]

# Liczba pytań to liczba elementów listy
question_number = len(test_results)

# Liczymy poprawne odpowiedzi. True w sumie daje 1, więc wystarczy zliczać True.
correct_answers = 0
for answer in test_results:
    if answer:
        correct_answers += 1

# Błędne = wszystkie pytania minus poprawne
incorrect_answers = question_number - correct_answers

# Procent poprawnych. Mnożymy przez 100 i dzielimy przez liczbę pytań.
# :.1f wypisze wynik z jednym miejscem po przecinku.
percent_correct = correct_answers / question_number * 100

print('TEST STATISTICS')
print('===============')
print('Number of questions:', question_number)
print('Number of correct answers:', correct_answers)
print('Number of incorrect answers:', incorrect_answers)
print(f'Percentage of correct answers: {percent_correct:.1f}%')
