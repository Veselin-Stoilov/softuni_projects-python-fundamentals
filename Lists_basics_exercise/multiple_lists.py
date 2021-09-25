factor = int(input())
count = int(input())
multiples_list = []
for num in range(factor, factor * count + 1, factor):
    multiples_list.append(num)
print(multiples_list)
