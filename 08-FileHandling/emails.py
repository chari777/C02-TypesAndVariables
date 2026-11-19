# KROKI (wspólne dla funkcji):
# 1. _read_email() wczytuje plik email.txt.
# 2. re.search() szuka pierwszego dopasowania wzorca w tekście.
# 3. Jeśli znalazł (match nie jest None) -> group(1) zwraca to, co było w nawiasie ().
# 4. Treść maila: wszystko po pierwszej pustej linii (koniec nagłówków) -> \n\n.
###
# Moduł do odczytu danych z surowego maila (plik email.txt).
# Każda funkcja wyciąga jedną część maila przy pomocy wyrażeń regularnych.
#
import re

# Wczytuje cały plik z mailem. Funkcja pomocnicza, używana przez inne funkcje.
def _read_email():
    with open('email.txt', 'r', encoding='utf-8') as file:
        return file.read()

# Adres nadawcy: w nagłówku 'From:' jest w nawiasach ostrych < >
def email_sender():
    email = _read_email()
    # ^From: - linia zaczynająca się od 'From:' (re.M sprawia, że ^ działa dla każdej linii)
    # <([^>]+)> - tekst w nawiasach ostrych, który nie zawiera '>'
    match = re.search(r'^From:.*<([^>]+)>', email, re.M)
    return match.group(1) if match else ''

# Adres odbiorcy: to samo, ale w nagłówku 'To:'
def email_recipient():
    email = _read_email()
    match = re.search(r'^To:.*<([^>]+)>', email, re.M)
    return match.group(1) if match else ''

# Temat maila: tekst po 'Subject:'.
# (.*) - wszystko do końca linii (kropka nie łapie znaku nowej linii)
def email_subject():
    email = _read_email()
    match = re.search(r'^Subject:\s*(.*)$', email, re.M)
    return match.group(1) if match else ''

# Treść maila: wszystko po pierwszej pustej linii (koniec nagłówków).
# re.S sprawia, że kropka łapie także znaki nowej linii.
def email_body():
    email = _read_email()
    match = re.search(r'\r?\n\r?\n(.*)', email, re.S)
    return match.group(1).strip() if match else ''
