string = input()
my_list = string.split(', ')
my_list.reverse()
elements_count = len(my_list)
sheep_counter = 0

for position in range(0, elements_count):
    if my_list[position] == 'sheep':
        sheep_counter += 1
    elif my_list[position] == 'wolf':
        if position != 0:
            print(f'Oi! Sheep number {sheep_counter}! You are about to be eaten by a wolf!')
        else:
            print('Please go away and stop eating my sheep')