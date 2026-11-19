###
# Znajduje adresy z otrzymanych e-maili, które są na liście spamu (część wspólna zbiorów)
#
emails_received = {"john@example.com", "spam1@example.com", "spam2@example.com", "jane@example.com"}
spam_list = {"spam1@example.com", "spam2@example.com"}

# & - część wspólna: elementy obecne w OBU zbiorach
spam_emails = emails_received & spam_list
print("Spam emails:", spam_emails)
