num_of_symbols = int(input())
balanced = True
not_possible = False
closing_bracket = 0
opening_bracket = 0
bracket_list = ['(', ')']
for num in range(1, num_of_symbols + 1):
    symbol = input()
    if symbol not in bracket_list:
        continue
    if symbol == '(':
        opening_bracket += 1
    elif symbol == ')':
        closing_bracket += 1
    if closing_bracket != opening_bracket:
        balanced = False
    else:
        balanced = True
    if opening_bracket - 1 > closing_bracket:
        not_possible = True
    if closing_bracket > opening_bracket:
        not_possible = True
if not_possible:
    print('UNBALANCED')
else:
    if balanced:
        print('BALANCED')
    else:
        print('UNBALANCED')
