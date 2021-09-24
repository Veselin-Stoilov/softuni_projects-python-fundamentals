command = input()
guests_dict = {}
meals_list = []
unliked_meals = 0
while command != 'Stop':
    command = command.split('-')
    cmd = command[0]
    guest = command[1]
    meal = command[2]
    if cmd == 'Like':
        if guest not in guests_dict:
            guests_dict[guest] = []
        if meal not in guests_dict[guest]:
            guests_dict[guest].append(meal)
        else:
            command = input()
            continue
    if cmd == 'Unlike':
        if guest not in guests_dict:
            print(f'{guest} is not at the party.')
            command = input()
            continue
        else:
            if meal not in guests_dict[guest]:
                print(f"{guest} doesn't have the {meal} in his/her collection.")
                command = input()
                continue
            else:
                guests_dict[guest].remove(meal)
                unliked_meals += 1
                print(f"{guest} doesn't like the {meal}.")

    command = input()
for person, meals in sorted(guests_dict.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])):
    print(f'{person}: {", ".join(meals)}')
print(f'Unliked meals: {unliked_meals}')
