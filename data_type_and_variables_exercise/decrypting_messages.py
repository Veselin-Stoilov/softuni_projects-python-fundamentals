key = int(input())
number_of_lines = int(input())
message = ''
for num in range(1, number_of_lines + 1):
    symbol = input()
    symbol = ord(symbol) + key
    symbol = chr(symbol)
    message += symbol
print(message)