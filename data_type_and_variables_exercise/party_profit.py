party_size = int(input())
days = int(input())
coins_counter = 0
for day in range(1, days+1):
    if day % 10 == 0:
        party_size -= 2
    if day % 15 == 0:
        party_size += 5
    coins_counter += 50
    coins_counter -= 2 * party_size
    if day % 3 == 0:
        coins_counter -= 3 * party_size
    if day % 5 == 0:
        coins_counter += 20 * party_size
        if day % 3 == 0:
            coins_counter -= 2 * party_size

coins_per_companion = int(coins_counter / party_size)
print(f'{party_size} companions received {coins_per_companion} coins each.')