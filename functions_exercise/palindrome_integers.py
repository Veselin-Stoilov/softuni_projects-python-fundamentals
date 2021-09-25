def palindrome_check(some_list):
    for num in some_list:
        num_reversed = num[::-1]
        if num == num_reversed:
            print('True')
        else:
            print('False')



my_list = input().split(', ')
palindrome_check(my_list)