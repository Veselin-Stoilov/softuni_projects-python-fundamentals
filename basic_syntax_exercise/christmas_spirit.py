allowed_quantity = int(input()) # of one type of decoration
days_left = int(input())
ornament_set_price = 2
tree_skirt_price = 5
tree_garlands_price = 3
tree_lights_price = 15
day_counter = 1
spirit = 0
money_spent = 0
while day_counter <= days_left:
    if day_counter % 2 == 0:
        spirit += 5
        money_spent += allowed_quantity * ornament_set_price
    if day_counter % 3 == 0:
        spirit += 13
        money_spent += allowed_quantity * (tree_skirt_price + tree_garlands_price)
    if day_counter % 5 == 0:
        spirit += 17
        money_spent += allowed_quantity * tree_lights_price
        if day_counter % 3 == 0:
            spirit += 30
    if day_counter % 10 == 0:
        spirit -= 20
        money_spent += tree_skirt_price + tree_garlands_price + tree_lights_price
    if day_counter % 11 == 0:
        allowed_quantity += 2
    day_counter += 1
if days_left % 10 == 0:
    spirit -= 30
print(f'Total cost: {money_spent}')
print(f'Total spirit: {spirit}')


