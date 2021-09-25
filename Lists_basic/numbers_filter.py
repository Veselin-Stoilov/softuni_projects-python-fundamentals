n = int(input())
even_list = []
odd_list = []
negative_list = []
positive_list = []
for _ in range(n):
    num = int(input())
    if num % 2 == 0:
        even_list.append(num)
    if num % 2 != 0:
        odd_list.append(num)
    if num < 0:
        negative_list.append(num)
    if num >= 0:
        positive_list.append(num)
filter = input()
if filter == 'even':
    print(even_list)
elif filter == 'odd':
    print(odd_list)
elif filter == 'negative':
    print(negative_list)
elif filter == 'positive':
    print(positive_list)
