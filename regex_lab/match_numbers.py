text = input()
import re
pattern = r'(^|(?<=\s))-?[0-9]*\.?[0-9]*((?=\s)|$)'
valid_nums = re.finditer(pattern, text)
valid_nums_lst = []

for num in valid_nums:
    valid_nums_lst.append(num.group())
print(' '.join(valid_nums_lst))
