word = input()
word_lower = word.lower()
word_len = len(word)
index_list = []
for i in range(0, word_len):
    if word_lower[i] != word[i]:
        index_list.append(i)
print(index_list)

