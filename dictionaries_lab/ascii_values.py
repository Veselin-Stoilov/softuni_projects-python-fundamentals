chars = input().split(', ')
chars_ascii_dict = {}
# for char in chars:
#     chars_ascii_dict[char] = ord(char)

chars_ascii_dict = {char: ord(char) for char in chars}
print(chars_ascii_dict)