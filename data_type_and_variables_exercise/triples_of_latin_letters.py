n = int(input())
for num_1 in range(97, 97 + n):
    for num_2 in range(97, 97 + n):
        for num_3 in range(97, 97 + n):
            print(f'{chr(num_1)}{chr(num_2)}{chr(num_3)}')
