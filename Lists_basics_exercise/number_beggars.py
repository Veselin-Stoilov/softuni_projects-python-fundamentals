integers_string = input()
beggars_count = int(input())
integers_list = integers_string.split(', ')
profit_list = []
for beggar in range(beggars_count):
    amount_counter = 0
    for amount in integers_list[beggar: len(integers_list): beggars_count]:
            amount = int(amount)
            amount_counter += amount
    profit_list.append(amount_counter)
print(profit_list)


