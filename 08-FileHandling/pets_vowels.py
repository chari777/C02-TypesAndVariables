###
# Zlicza samogłoski w tekście wpisanym z klawiatury (wyrażenia regularne)
#
import re

text = input('Enter text: ')

# [aeiou] - dowolna z pięciu samogłosek. flags=re.I ignoruje wielkość liter.
vowels = re.findall(r'[aeiou]', text, flags=re.I)
print('Number of vowels:', len(vowels))
