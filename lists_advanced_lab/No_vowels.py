word_str = input()
vowels_list = ['a', 'o', 'u', 'e', 'i']
no_vowels = [letter for letter in word_str \
if letter.lower() not in vowels_list]
print(''.join(no_vowels))