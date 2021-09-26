data = input()
import re
order_list = []
cost = 0
pattern = r'>>(?P<item>[A-Za-z]+)<<(?P<price>[0-9\.]+)\!(?P<quantity>[0-9]+)'
while data != 'Purchase':
    order = re.match(pattern, data)
    if order:
        item = order.group('item')
        price = float(order.group('price'))
        quantity = int(order.group('quantity'))
        cost += price * quantity
        order_list.append(item)
    data = input()
print('Bought furniture:')
for i in order_list:
    print(i)
print(f'Total money spend: {cost:.2f}')

