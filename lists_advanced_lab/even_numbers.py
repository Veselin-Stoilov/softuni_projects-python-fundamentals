nums_list = [int(num) for num in input().split(', ')]
even_indexes_list = []
for num in nums_list:
    if num % 2 == 0:
        even_indexes_list.append(nums_list.index(num))
print(even_indexes_list)
