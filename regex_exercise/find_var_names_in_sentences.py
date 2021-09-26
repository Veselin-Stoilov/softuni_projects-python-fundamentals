text = input()
import re
valid_vars = []
pattern = r'(?<= _)[A-Za-z0-9]+\b'

valid_data = re.findall(pattern, text)
for var in valid_data:
    valid_vars.append(var)
print(','.join(valid_vars))
