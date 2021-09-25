def order_sum(item, amount):
    if item == 'coffee':
        sum = amount * 1.50
        return sum
    elif item == 'water':
        sum = amount * 1
        return sum
    elif item == 'coke':
        sum = amount * 1.40
        return sum
    elif item == 'snacks':
        sum = amount * 2
        return sum


ordered_item = input()
ordered_amount = int(input())
total_sum = order_sum(ordered_item, ordered_amount)
print(f'{total_sum:.2f}')