def find_substrings(substring, full_string):
    substring_list = []
    for word_1 in substring:
        for word_2 in full_string:
            if word_1 in word_2:
                substring_list.append(word_1)
                break
    return substring_list


substring_collection = input().split(', ')
full_string_collection = input().split(', ')
print(find_substrings(substring_collection, full_string_collection))

