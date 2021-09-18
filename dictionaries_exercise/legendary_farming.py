def mayterials_collection(key_materials_dict, junk_materials_dict, material, quantity):
    if material in key_materials_dict.keys():
        key_materials_dict[material] += quantity
    else:
        if material not in junk_materials_dict.keys():
            junk_materials_dict[material] = quantity
        else:
            junk_materials_dict[material] += quantity


key_materials_dict = {'shards': 0, 'fragments': 0, 'motes': 0}
junk_materials_dict = {}
legendary_item = ''
while legendary_item == '':
    materials = input().split(' ')
    materials = [int(x) if x.isnumeric() else x.lower() for x in materials]
    for i in range(0, len(materials), 2):
        # material = materials[i + 1].lower()
        # quantity = int(materials[i])
        material = materials[i + 1]
        quantity = materials[i]

        mayterials_collection(key_materials_dict, junk_materials_dict, material, quantity)

        if key_materials_dict['shards'] >= 250:
            legendary_item = 'Shadowmourne'
            key_materials_dict['shards'] -= 250
            break
        elif key_materials_dict['fragments'] >= 250:
            legendary_item = 'Valanyr'
            key_materials_dict['fragments'] -= 250
            break
        elif key_materials_dict['motes'] >= 250:
            legendary_item = 'Dragonwrath'
            key_materials_dict['motes'] -= 250
            break

print(f'{legendary_item} obtained!')
for material, quantity in sorted(key_materials_dict.items(), key=lambda kvp: (-kvp[1], kvp[0])):
    print(f'{material}: {quantity}')
for material, quantity in sorted(junk_materials_dict.items(), key=lambda kvp: kvp[0]):
    print(f'{material}: {quantity}')



