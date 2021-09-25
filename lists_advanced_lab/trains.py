n_wagons = int(input())
command = input()
train = [0] * n_wagons

while not command == 'End':
    if 'add' in command:
        add_pax = command.split()
        added_pax = int(add_pax[1])
        train[-1] += added_pax
    elif 'insert' in command:
        insert_people = command.split()
        inserted_pax = int(insert_people[2])
        index_wagon = int(insert_people[1])
        train[index_wagon] += inserted_pax
    elif 'leave' in command:
        leave_people = command.split()
        left_pax = int(leave_people[2])
        index_wagon = int(leave_people[1])
        train[index_wagon] -= left_pax
    command = input()
print(train)



