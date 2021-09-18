words = input().split(' ')
odd_words_dict = {}
odd_words = []
words = [x.lower() for x in words]
for word in words:
    if word not in odd_words_dict:
        odd_words_dict[word] = 1
    else:
        odd_words_dict[word] += 1
for word, quantity in odd_words_dict.items():
    if quantity % 2 != 0:
        odd_words.append(word)
print(' '.join(odd_words))