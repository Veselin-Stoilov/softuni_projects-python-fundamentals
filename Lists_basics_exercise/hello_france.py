items_string = input()
budget = float(input())
tickets_price = 150
money_left = budget
profit = 0
income = 0
new_prices = []
item_price_list = items_string.split('|')
for item in item_price_list:
    item_price = item.split('->')
    item_price[1] = float(item_price[1])
    if item_price[0] == 'Clothes':
        if item_price[1] > 50:
            continue
    elif item_price[0] == 'Shoes':
        if item_price[1] > 35:
            continue
    elif item_price[0] == 'Accessories':
        if item_price[1] > 20.50:
            continue
    if money_left < item_price[1]:
        continue
    money_left -= item_price[1]
    item_new_price = item_price[1] * 1.4
    item_new_price = round(item_new_price, 2)
    new_prices.append(item_new_price)
    income += item_new_price
profit = income - budget
print(new_prices)
print(f'Profit: {profit:.2f}')
if (income + money_left) >= tickets_price:
    print('Hello, France!')
print(income)
