word = input()
word_len = int(len(word))
reverse_word = ''
# for letter in word:
#     reverse_word = letter + reverse_word
# print(reversed(reverse_word))
# print(word[::-1])

for item in range(word_len-1, -1, -1):
    reverse_word += word[item]
print(reverse_word)