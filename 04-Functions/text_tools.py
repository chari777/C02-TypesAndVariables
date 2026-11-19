###
# Moduł z funkcją liczącą wystąpienia litery w tekście
#
def count_letter(text, letter):
    # count() to metoda napisu, która zlicza, ile razy dany fragment
    # występuje w tekście. Liczy wielkość liter, więc 'e' != 'E'.
    return text.count(letter)
