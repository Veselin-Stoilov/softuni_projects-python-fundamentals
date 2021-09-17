number = input()

for num in range(9, -1, -1):
    for digit in number:
        digit = int(digit)
        if num == digit:
            print(digit, end='')

