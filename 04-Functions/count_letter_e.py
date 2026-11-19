###
# Program liczy, ile razy litera 'e' występuje w podanym tekście.
from text_tools import count_letter

text = 'You never get a second chance to make a first impression'
letter = 'e'

print(text)
print(f"The number of letter '{letter}': {count_letter(text, letter)}")
