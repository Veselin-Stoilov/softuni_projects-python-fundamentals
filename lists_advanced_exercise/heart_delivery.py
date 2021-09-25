neighborhood = input().split('@')
neighborhood = [int(x) for x in neighborhood]
num_of_houses = len(neighborhood)
current_index = 0
cmd = input()
no_valentines_day_counter = 0
has_failed = False
while cmd != 'Love!':
    cmd = cmd.split(' ')
    jump_length = int(cmd[1])
    current_index += jump_length
    if current_index + 1 > num_of_houses:
        current_index = 0
    if neighborhood[current_index] == 0:
        print(f"Place {current_index} already had Valentine's day.")
    else:
        neighborhood[current_index] -= 2
        if neighborhood[current_index] == 0:
            print(f"Place {current_index} has Valentine's day.")

    cmd = input()
print(f"Cupid's last position was {current_index}.")
for house in neighborhood:
    if house != 0:
        no_valentines_day_counter += 1
        has_failed = True
if has_failed:
    print(f"Cupid has failed {no_valentines_day_counter} places.")
else:
    print('Mission was successful.')

