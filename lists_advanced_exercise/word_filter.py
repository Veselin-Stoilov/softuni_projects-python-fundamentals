sentence = input().split(' ')
even_len_words = [word for word in sentence if len(word) % 2 == 0]
for el in even_len_words:
    print(el)