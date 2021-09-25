nums_str = input()
nums_to_remove = int(input())
nums_list = nums_str.split()
for i in range(len(nums_list)):
    nums_list[i] = int(nums_list[i])
for _ in range(nums_to_remove):
    min_num = min(nums_list)
    nums_list.remove(min_num)
print(nums_list)

