first_string = input()
second_string = input()
mutate_string = ''
word_len = len(first_string)

for position in range(0, word_len):
    if first_string[position] == second_string[position]:
        continue
    print(second_string[:position+1], end='')
    print(first_string[position+1:])




