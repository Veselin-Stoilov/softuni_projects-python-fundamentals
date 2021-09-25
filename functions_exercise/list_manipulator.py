import sys


def exchange(my_list, command):
    index = int(command[1])
    if index not in range(len(my_list) - 1):
        return 'Invalid index'
    else:
        sub_list_1 = my_list[:index + 1]
        sub_list_2 = my_list[index + 1:]
        changed_list = sub_list_2 + sub_list_1
        return changed_list


def max_even_odd(my_list, command):
    max_odd = - sys.maxsize
    max_even = - sys.maxsize
    odd_found = False
    even_found = False
    if command[1] == 'odd':
        for index, el in enumerate(my_list):
            if el % 2 != 0:
                odd_found = True
                if el >= max_odd:
                    max_odd = el
                    max_odd_index = index
        if not odd_found:
            return 'No matches'
        else:
            return max_odd_index
    if command[1] == 'even':
        for index, el in enumerate(my_list):
            if el % 2 == 0:
                even_found = True
                if el >= max_even:
                    max_even = el
                    max_even_index = index
        if not even_found:
            return 'No matches'
        else:
            return max_even_index


def min_even_odd(my_list, command):
    min_odd = sys.maxsize
    min_even = sys.maxsize
    odd_found = False
    even_found = False
    if command[1] == 'odd':
        for index, el in enumerate(my_list):
            if el % 2 != 0:
                odd_found = True
                if el <= min_odd:
                    min_odd = el
                    min_odd_index = index
        if not odd_found:
            return 'No matches'
        else:
            return min_odd_index
    if command[1] == 'even':
        for index, el in enumerate(my_list):
            if el % 2 == 0:
                even_found = True
                if el <= min_even:
                    min_even = el
                    min_even_index = index
        if not even_found:
            return 'No matches'
        else:
            return min_even_index


def first_even_odd(my_list, command):
    even_list = []
    odd_list = []
    even_counter = 0
    odd_counter = 0
    count = int(command[1])
    if count > len(my_list):
        return 'Invalid count'
    if command[2] == 'even':
        for num in my_list:
            if num % 2 == 0:
                even_counter += 1
                even_list.append(num)
            if even_counter == count:
                return even_list
        return even_list
    if command[2] == 'odd':
        for num in my_list:
            if num % 2 != 0:
                odd_counter += 1
                odd_list.append(num)
            if odd_counter == count:
                return odd_list
        return odd_list


def last_even_odd(my_list, command):
    even_list = []
    odd_list = []
    even_counter = 0
    odd_counter = 0
    count = int(command[1])
    if count > len(my_list):
        return 'Invalid count'
    if command[2] == 'even':
        for num in my_list[::-1]:
            if num % 2 == 0:
                even_counter += 1
                even_list.append(num)
            if even_counter == count:
                return even_list[::-1]
        return even_list
    if command[2] == 'odd':
        for num in my_list[::-1]:
            if num % 2 != 0:
                odd_counter += 1
                odd_list.append(num)
            if odd_counter == count:
                return odd_list[::-1]
        return odd_list


my_current_list = input().split(' ')
my_list_int = [int(num) for num in my_current_list]
current_command = input()
list_changed = False
while current_command != 'end':
    current_command = current_command.split(' ')
    if 'exchange' in current_command:
        if list_changed:
            print(exchange(my_list_int, current_command), current_command)
        else:
            print(exchange(my_list_int, current_command))
        list_changed = True
    elif 'max' in current_command:
        if list_changed:
            print(max_even_odd(exchange(my_list_int, current_command), current_command))
        else:
            print(max_even_odd(my_list_int, current_command))
    elif 'first' in current_command:
        if list_changed:
            print(first_even_odd(exchange(my_list_int, current_command), current_command))
        else:
            print(first_even_odd(my_list_int, current_command))
    elif 'last' in current_command:
        if list_changed:
            print(last_even_odd(my_list_int, current_command), current_command)
        else:
            print(last_even_odd(my_list_int, current_command))
    current_command = input()



