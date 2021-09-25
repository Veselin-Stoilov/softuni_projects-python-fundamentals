n = int(input())
word = input()
my_list = []
filtered_list = []
for _ in range(n):
    sentence = input()
    my_list.append(sentence)
    if word in sentence:
        filtered_list.append(sentence)
print(my_list)
print(filtered_list)