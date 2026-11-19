###
# Usuwa duplikaty adresów e-mail za pomocą zbioru (set)
#
emails = ["john@example.com", "jane@example.com", "john@example.com", "alex@example.com"]

# set() tworzy zbiór - w zbiorze każdy element występuje tylko raz
unique_emails = set(emails)
print(unique_emails)
