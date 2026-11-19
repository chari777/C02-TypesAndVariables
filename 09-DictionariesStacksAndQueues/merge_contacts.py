###
# Łączy dwie listy kontaktów i usuwa duplikaty (suma zbiorów)
#
contacts_A = {"john@example.com", "alice@example.com", "bob@example.com"}
contacts_B = {"bob@example.com", "michael@example.com", "sara@example.com"}

# | - suma zbiorów: wszystkie elementy z obu zbiorów, bez powtórzeń
merged_contacts = contacts_A | contacts_B
print("Merged contacts:", merged_contacts)
