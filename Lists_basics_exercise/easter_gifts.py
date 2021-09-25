gifts_string = input()
gifts_list = gifts_string.split()
command = input()
while command != 'No Money':
    if 'OutOfStock' in command:
        out_of_stock_list = command.split()
        for index, value in enumerate(gifts_list):
            if value == out_of_stock_list[1]:
                gifts_list[index] = 'None'
    elif 'Required' in command:
        required_list = command.split()
        if int(required_list[2]) < len(gifts_list):
            gifts_list[int(required_list[2])] = required_list[1]
    elif 'JustInCase' in command:
        just_in_case_list = command.split()
        gifts_list[-1] = just_in_case_list[1]
    command = input()
for value in gifts_list:
    if value == 'None':
        gifts_list.remove(value)
print(*gifts_list, sep = ' ')