n = int(input())
register_dict = {}
for _ in range(n):
    command = input().split()
    action = command[0]
    name = command[1]
    if action == 'register':
        car_reg = command[2]
        if name in register_dict:
            print(f'ERROR: already registered with plate number {car_reg}')
        else:
            register_dict[name] = car_reg
            print(f'{name} registered {car_reg} successfully')
    if action == 'unregister':
        if name not in register_dict:
            print(f'ERROR: user {name} not found')
        else:
            register_dict.pop(name)
            print(f'{name} unregistered successfully')
for name, car_reg in register_dict.items():
    print(f'{name} => {car_reg}')
