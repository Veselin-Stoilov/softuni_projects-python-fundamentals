kvp = input()
bakery_dict = {}

while kvp != 'statistics':
    kvp = kvp.split(': ')
    key, value = kvp
    if kvp[0] not in bakery_dict:
        bakery_dict[key] = int(value)
    else:
        bakery_dict[key] += int(value)
    kvp = input()
print('Products in stock:')
# for product, quantity in bakery_dict.items():
#     print(f'- {product}: {quantity}')
[print(f"- {product}: {quantity}") for product, quantity in bakery_dict.items()]
print(f'Total Products: {len(bakery_dict)}')
print(f'Total Quantity: {sum(bakery_dict.values())}')
