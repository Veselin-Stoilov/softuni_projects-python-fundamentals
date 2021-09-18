lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
expenses_counter = 0
broken_shield_counter = 0
for game in range(1, lost_fights + 1):
    if game % 2 == 0:
        expenses_counter += helmet_price
    if game % 3 == 0:
        expenses_counter += sword_price
        if game % 2 == 0:
            expenses_counter += shield_price
            broken_shield_counter += 1
            if broken_shield_counter % 2 == 0:
                expenses_counter += armor_price
print(f'Gladiator expenses: {expenses_counter:.2f} aureus')