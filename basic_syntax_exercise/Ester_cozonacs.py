budget = float(input())
flour_price = float(input()) #price/kg
eggs_price = flour_price * 0.75
milk_price_1_liter = flour_price * 1.25
cozonac_price = eggs_price + flour_price + milk_price_1_liter/4
colored_eggs_counter = 0
cozonac_counter = 0
lost_eggs = 0
money_left = budget
while money_left > 0:
    if money_left < cozonac_price:
        break
    cozonac_counter += 1
    colored_eggs_counter += 3
    if cozonac_counter % 3 == 0:
        lost_eggs = cozonac_counter - 2
        colored_eggs_counter -= (cozonac_counter - 2)
    money_left -= cozonac_price
print(f'You made {cozonac_counter} cozonacs! Now you have {colored_eggs_counter} eggs and {money_left:.2f}BGN left.')
