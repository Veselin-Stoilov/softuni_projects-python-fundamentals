text = input()
import re
pattern = r'(?P<email>^|(?<=\s)[a-zA-Z1-9]+[\-\.\_]*[a-zA-Z1-9]+@[a-zA-Z]+[\-]*[a-zA-Z]+\.+' \
          r'[a-zA-Z]+[A-Za-z\-|\.]*[a-zA-Z](?=(\,|\.|\s))|$)'
valid_emails = []
valid_data = re.finditer(pattern, text)
for email in valid_data:
    valid_emails.append(email.group('email'))

for mail in valid_emails:
    print(mail)

