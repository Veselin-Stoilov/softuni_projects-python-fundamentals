nums_list = input().split(', ')
positive = ', '.join([num for num in nums_list if int(num) >= 0])
negative = ', '.join([num for num in nums_list if int(num) < 0])
even = ', '.join([num for num in nums_list if int(num) % 2 == 0])
odd = ', '.join([num for num in nums_list if int(num) % 2 != 0])

print(f'Positive: {positive}')
print(f'Negative: {negative}')
print(f'Even: {even}')
print(f'Odd: {odd}')

