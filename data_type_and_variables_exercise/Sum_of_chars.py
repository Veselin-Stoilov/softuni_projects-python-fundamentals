n = int(input())
ord_counter = 0
for num in range(n):
    char = input()
    ord_counter += ord(char)
print(f'The sum equals: {ord_counter}')
