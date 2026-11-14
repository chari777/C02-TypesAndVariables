name = 'Gabriel'
surname = 'Kozicki'

characters_in_name = len(name) # funkcja len() liczy długość tekstu (ile jest znaków)
print(f'Your name has {characters_in_name} characters')
print(f'Your surname has {len(surname)} characters')

full_name = name + ' ' + surname
print(f'Your full name has {len(full_name)} characters') # pamiętam, że spacja w środku też liczy się jako znak