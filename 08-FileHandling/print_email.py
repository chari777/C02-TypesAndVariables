###
# Program wypisuje dane z maila, korzystając z funkcji z modułu emails.py
#
import emails

print('Sender:', emails.email_sender())
print('Recipient:', emails.email_recipient())
print('Subject:', emails.email_subject())
print('Body:')
print(emails.email_body())
