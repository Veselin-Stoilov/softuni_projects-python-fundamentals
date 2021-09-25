def password_validator(password: str):
    digit_counter = 0
    len_is_valid = False
    alnum_is_valid = False
    min_2_digits = False
    if 6 <= len(password) <= 10:
        len_is_valid = True
    else:
        print('Password must be between 6 and 10 characters')
    if password.isalnum():
        alnum_is_valid = True
    else:
        print("Password must consist only of letters and digits")
    for el in password:
        if el.isnumeric():
            digit_counter += 1
    if digit_counter >= 2:
        min_2_digits = True
    else:
        print('Password must have at least 2 digits')
    if len_is_valid == True and alnum_is_valid == True and min_2_digits == True:
        print('Password is valid')


password = input()
password_validator(password)