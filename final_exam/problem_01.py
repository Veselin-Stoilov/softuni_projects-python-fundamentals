name = input()

command = input()

while command != 'Sign up':
    command = command.split(' ')
    if 'Case' in command:
        letters_size = command[1]
        if letters_size == 'lower':
            name = name.lower()
        elif letters_size == 'upper':
            name = name.upper()
        print(name)
    elif 'Reverse' in command:
        start_index = int(command[1])
        end_index = int(command[2])
        if end_index >= len(name):
            command = input()
            continue
        else:
            substring = name[start_index: end_index + 1]
            reversed_sub = substring[::-1]
            print(reversed_sub)
    elif 'Cut' in command:
        substring = command[1]
        if substring in name:
            name = name.replace(substring, '')
            print(name)
        else:
            print(f"The word {name} doesn't contain {substring}.")
    elif 'Replace' in command:
        char = command[1]
        if char in name:
            while char in name:
                name = name.replace(char, '*')
            print(name)
        else:
            command = input()
            continue
    elif 'Check' in command:
        char = command[1]
        if char in name:
            print('Valid')
        else:
            print(f'Your username must contain {char}.')
    command = input()


