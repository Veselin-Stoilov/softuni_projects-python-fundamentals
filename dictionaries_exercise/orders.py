product_info = input()
products_dict = {}
while product_info != 'buy':
    product_info = product_info.split()
    name = product_info[0]
    price = float(product_info[1])
    quantity = int(product_info[2])
    price_quantity = [price, quantity]

    if name not in products_dict:
        products_dict[name] = price_quantity
    else:
        products_dict[name][0] = price
        products_dict[name][1] += quantity
    product_info = input()
for key, value in products_dict.items():
    print(f'{key} -> {value[0] * value[1]:.2f}')
