command = input()
side_dict = {}
user_already_exists = False
while command != 'Lumpawaroo':
    if ' | ' in command:
        command = command.split(' | ')
        side = command[0]
        user = command[1]
        for value in side_dict.values():
            if value == user:
                user_already_exists = True
                break
        if user_already_exists:
            command = input()
            break
        side_dict[side] = [user]
    elif ' -> ' in command:
        user_already_exists = False
        command = command.split(' -> ')
        user = command[0]
        side = command[1]
        for key, value in side_dict.items():
            if user in value:
                user_already_exists = True
                side_dict[key].remove(user)
                break
        if user_already_exists:
            side_dict[side].append(user)
            print(f'{user} joins the {side} side!')
        if not user_already_exists:
            if side in side_dict:
                side_dict[side].append(user)
            else:
                side_dict[side] = [user]
            print(f'{user} joins the {side} side!')
    command = input()
for key, value in sorted(side_dict.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])):
    if len(value) > 0:
        print(f'Side: {key}, Members: {len(value)}')
        value = sorted(value)
        for name in value:
            print(f'! {name}')


