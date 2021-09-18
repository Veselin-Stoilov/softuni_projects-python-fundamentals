number = int(input())
special_list = [5, 7, 11]
# for num in range(1, number + 1):
#     num = str(num)
#     digit_sum = 0
#     for digit in num:
#         digit = int(digit)
#         digit_sum += digit
#     if digit_sum in special_list:
#         print(f'{num} -> True')
#     else:
#         print(f'{num} -> False')

for num in range(1, number + 1):
    sum = 0
    digits = num
    while digits > 0:
        last_digit = digits % 10
        digits = digits // 10
        sum += last_digit
    if sum in special_list:
        print(f'{num} -> True')
    else:
        print(f'{num} -> False')