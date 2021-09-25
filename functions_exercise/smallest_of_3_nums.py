def smallest_num(n_1, n_2, n_3):
    my_list = [n_1, n_2, n_3]
    return min(my_list)


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
print(smallest_num(num_1, num_2, num_3))