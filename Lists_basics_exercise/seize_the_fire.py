type_fire_cell_value = input() #High/Medium/Low
water = int(input())
effort = 0
total_effort = 0
total_fire = 0
fires_list = type_fire_cell_value.split('#')
print('Cells:')
for fire in fires_list:
    fire_value_list = fire.split(' = ')
    fire_value_list[1] = int(fire_value_list[1])
    if fire_value_list[0] == 'High':
        if fire_value_list[1] not in range(81, 126):
            continue
    elif fire_value_list[0] == 'Medium':
        if fire_value_list[1] not in range(51, 81):
            continue
    elif fire_value_list[0] == 'Low':
        if fire_value_list[1] not in range(1, 51):
            continue
    if water < fire_value_list[1]:
        continue
    else:
        water -= fire_value_list[1]
        total_effort += 0.25 * fire_value_list[1]
        total_fire += fire_value_list[1]

        print(f' - {fire_value_list[1]}')
print(f'Effort: {total_effort}')
print(f'Total Fire: {total_fire}')
