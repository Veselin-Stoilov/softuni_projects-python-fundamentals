n = int(input())
positive_list = []
negative_list = []
for _ in range(n):
    num = int(input())
    if num < 0:
        negative_list.append(num)
    else:
        positive_list.append(num)
count_positives = len(positive_list)
sum_negatives = sum(negative_list)
print(positive_list)
print(negative_list)
print(f'Count of positives: {count_positives}. Sum of negatives: {sum_negatives}')