inventory = input().split(' ')
searched_products = input().split(' ')
invent_dict = {}
for i in range(0, len(inventory), 2):
    key = inventory[i]
    value = inventory[i + 1]
    invent_dict[key] = int(value)
for product in searched_products:
    if product in invent_dict:
        if invent_dict[product] > 0:
            print(f'We have {invent_dict[product]} of {product} left')
    else:
        print(f"Sorry, we don't have {product}")

