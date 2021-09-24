n = int(input())
reg_counter = 0
import re
pattern = r'U\$([A-Z][a-z]{2,})U\$P\@\$([A-Za-z]{5,}[0-9]+)P\@\$'
for i in range(n):
    command = input()
    valid_reg = re.findall(pattern, command)
    if valid_reg:
        reg_counter += 1
        for match in valid_reg:
            name = match[0]
            password = match[1]
            print('Registration was successful')
            print(f'Username: {name}, Password: {password}')

    else:

        print('Invalid username or password')
print(f'Successful registrations: {reg_counter}')


