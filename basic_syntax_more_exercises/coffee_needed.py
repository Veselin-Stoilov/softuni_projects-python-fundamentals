command = input()
command_upper_case = command.upper()
command_lower_case = command.lower()
coffee_cups_counter = 0
commands_list = ['coding', 'dog', 'cat', 'movie']
while command != 'END':
    if command_lower_case in commands_list:
        if command_lower_case == command:
            coffee_cups_counter += 1
        elif command_lower_case != command:
            coffee_cups_counter += 2
    command = input()
    command_upper_case = command.upper()
    command_lower_case = command.lower()
if coffee_cups_counter > 5:
    print('You need extra sleep')
else:
    print(coffee_cups_counter)
