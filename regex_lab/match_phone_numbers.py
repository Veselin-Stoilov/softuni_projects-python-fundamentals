text = input()
import re
valid_nums_list = []
pattern = r'\+359(?P<separator>( |-))2(?P=separator)[0-9]{3}(?P=separator)[0-9]{4}\b'

valid_numbers = re.finditer(pattern, text)
for num in valid_numbers:
    valid_nums_list.append(num.group())
print(', '.join(valid_nums_list))