command = input()
elements_list = []
elements_dict = {}
while command != 'stop':
    elements_list.append(command)
    command = input()
for i in range(0, len(elements_list), 2):
    if elements_list[i] not in elements_dict.keys():
        elements_dict[elements_list[i]] = int(elements_list[i + 1])
    else:
        elements_dict[elements_list[i]] += int(elements_list[i + 1])
for element, quantity in elements_dict.items():
    print(f'{element} -> {quantity}')

