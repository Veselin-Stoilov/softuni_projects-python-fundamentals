text = input()
import re
pattern = r'[0-9]+'
nums_list = []
while text != '':
    valid_nums = re.findall(pattern, text)
    for num in valid_nums:
        nums_list.append(num)
    text = input()
print(' '.join(nums_list))