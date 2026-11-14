plain_text = 'The early bird catches the worm'
encrypted_text = '' # tu będę zbierać zaszyfrowane znaki

for char in plain_text:
    code = ord(char)        # zamieniam znak na jego numer w tabeli kodów komputera
    new_code = code + 1     # przesuwam kod o 1 miejsce w prawo (np. A -> B)
    new_char = chr(new_code) # zamieniam nowy numer z powrotem na znak
    encrypted_text = encrypted_text + new_char # doklejam zaszyfrowany znak do wyniku

print(plain_text)
print(encrypted_text)