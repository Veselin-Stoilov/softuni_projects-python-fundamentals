number = int(input())
stars_counter = 0
stars_str = '*'
stars_pattern = ''

for num in range(1, number+1):
    for i in range(1, num + 1):
        print('*', end='')
    print()
for num in range(number, 1, -1):
    for i in range(num, 1, -1):
        print('*', end='')
    print()

# for num in range(1, number + 1):
#     stars_counter += 1
#     stars_pattern += stars_str[0]
#     print(stars_pattern)
# for num in range(1, number + 1):
#     stars_pattern = stars_pattern[:-1]
#     print(stars_pattern)