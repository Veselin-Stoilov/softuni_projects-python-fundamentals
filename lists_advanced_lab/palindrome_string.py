words_list = input().split()
searched_word = input()
palindrome_list = [word for word in words_list if word == word[::-1]]
searched_palindrome = palindrome_list.count(searched_word)
print(palindrome_list)
print(f'Found palindrome {searched_palindrome} times')