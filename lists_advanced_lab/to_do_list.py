command = input()
to_do_list = [0] * 10
while not command == 'End':
    importance, note = command.split('-')
    to_do_list.insert(int(importance), note)
    command = input()
result = [el for el in to_do_list if el != 0]
print(result)