num_str = input()
num_list = num_str.split()
inverted_list = []
for i in range(len(num_list)):
    num_list[i] = int(num_list[i])
    inverted_list.append(num_list[i] * -1)
print(inverted_list)