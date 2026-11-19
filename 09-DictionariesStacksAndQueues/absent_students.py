###
# Wyszukuje nieobecnych studentów: różnica zbiorów (wszyscy minus obecni)
#
all_students = {"Alice", "John", "Sara", "Bob"}
attended_students = {"Alice", "Bob"}

# Operator - zwraca elementy, które są w pierwszym zbiorze, a nie ma ich w drugim
absent_students = all_students - attended_students
print(absent_students)
