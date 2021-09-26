text = input().lower()
word = input().lower()
import re
pattern = rf'\b{word}[\.|\?|\!]*\b'
word_counter = len(re.findall(pattern, text))
print(word_counter)
