text = input()
import re

pattern = r'\b(?P<first_name>[A-Z][a-z]+) (?P<second_name>[A-Z][a-z]+)\b'

valid_names = re.finditer(pattern, text)
for name in valid_names:
    print(name.group(), end=' ')