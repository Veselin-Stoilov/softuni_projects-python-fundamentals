n = int(input())
liters_counter = 0
for num in range(0, n):
    added_water = int(input())
    liters_counter += added_water
    if liters_counter > 250:
        print('Insufficient capacity!')
        liters_counter -= added_water
print(liters_counter)