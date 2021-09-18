text = input()
chars_count = {}
for char in text:
    if char != ' ':
        if char not in chars_count:
            chars_count[char] = 0
        chars_count[char] += 1
for key, value in chars_count.items():
    print(f'{key} -> {value}')