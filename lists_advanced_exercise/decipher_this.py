def message_decoder(coded_string):
    decoded_message = []
    for word in coded_string:
        coded_letter = ''
        reg_letters = ''
        decoded_word = ''
        for letter in word:
            if letter.isnumeric():
                coded_letter += letter
            if letter.isalpha():
                reg_letters += letter
        coded_letter = chr(int(coded_letter))
        reg_letters = list(reg_letters)
        reg_letters[0], reg_letters[-1] = reg_letters[-1], reg_letters[0]
        reg_letters = ''.join(reg_letters)
        decoded_word = coded_letter + reg_letters
        decoded_message.append(decoded_word)
    decoded_message = ' '.join(decoded_message)
    print(decoded_message)


coded_string = input().split(' ')
message_decoder(coded_string)
