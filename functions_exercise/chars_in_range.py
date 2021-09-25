def ascii_chars_string(char_1, char_2):
    ascii_chars_list = []
    char_1_ord = ord(char_1)
    char_2_ord = ord(char_2)
    for num in range(char_1_ord + 1, char_2_ord):
        ascii_chars_list.append(chr(num))
    return ' '.join(ascii_chars_list)


ch_1 = input()
ch_2 = input()
print(ascii_chars_string(ch_1, ch_2))