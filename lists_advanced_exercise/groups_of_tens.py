def group_nums_in_groups_of_10s(int_list):
    max_num = max(int_list)
    highest_group_of_10s = (max_num // 10) * 10
    if max_num % 10 == 0:
        for group in range(10, highest_group_of_10s + 1, 10):
            group_list = []
            for num in int_list:
                if (group - 10) < num <= group:
                    group_list.append(num)
            print(f"Group of {group}'s: {group_list}")
    else:
        for group in range(10, highest_group_of_10s + 11, 10):
            group_list = []
            for num in int_list:
                if (group - 10) < num <= group:
                    group_list.append(num)
            print(f"Group of {group}'s: {group_list}")


el_list = input().split(', ')
nums_list = [int(num) for num in el_list]
group_nums_in_groups_of_10s(nums_list)