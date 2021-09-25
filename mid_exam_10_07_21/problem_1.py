count_of_orders = int(input())
total_price = 0
for order in range(1, count_of_orders + 1):
    capsule_price = float(input())
    days = int(input())
    capsules_count = int(input())
    coffee_price = days * capsules_count * capsule_price
    total_price += coffee_price
    print(f'The price for the coffee is: ${coffee_price:.2f}')
print(f'Total: ${total_price:.2f}')