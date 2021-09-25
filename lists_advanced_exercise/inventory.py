def inventory_list(items_list, cmd):
    cmd = cmd.split(' - ')
    action = cmd[0]
    item = cmd[1]
    if action == 'Collect':
        if item not in items_list:
            items_list.append(item)
    elif action == 'Drop':
        if item in items_list:
            items_list.remove(item)
    elif action == 'Combine Items':
        old_item, new_item = item.split(':')[0], item.split(':')[1]
        if old_item in items_list:
            items_position_check = items_list
            for ind, it in enumerate(items_position_check):
                if old_item == it:
                    old_item_index = ind
                    items_list.insert((old_item_index + 1), new_item)
                    break
    elif action == 'Renew':
        if item in items_list:
            items_position_check = items_list
            for it in items_position_check:
                if item == it:
                    items_list.remove(item)
                    items_list.append(item)
                    break
    return items_list


items_list = input().split(', ')
cmd = input()
while cmd != 'Craft!':
    inventory_list(items_list, cmd)
    cmd = input()
items_list = ', '.join(items_list)
print(items_list)



