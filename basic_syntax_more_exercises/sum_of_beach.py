my_string = input()
my_string = my_string.lower()
beach_counter = 0
for index, letter in enumerate(my_string):
    if letter == 'w':
        if my_string[index:index + 5] == 'water':
            beach_counter += 1
    elif letter == 'f':
        if my_string[index: index + 4] == 'fish':
            beach_counter += 1
    elif letter == 's':
        if my_string[index: index + 3] == 'sun':
            beach_counter += 1
        elif my_string[index: index + 4] == 'sand':
            beach_counter += 1
print(beach_counter)



