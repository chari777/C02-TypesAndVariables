###
# Sprawdza, czy użytkownik ma wszystkie wymagane uprawnienia
#
required_permissions = {"read", "write", "execute"}
user_permissions = {"read", "write"}

# issubset() zwraca True, jeśli WSZYSTKIE wymagane uprawnienia są w zbiorze użytkownika
has_permissions = required_permissions.issubset(user_permissions)
print(has_permissions)   # False, bo brakuje "execute"
