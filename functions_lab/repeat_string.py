# def concatenate_string(string, counter):
#     new_string = string * counter
#     return new_string
#
#
my_string = input()
my_counter = int(input())
# print(concatenate_string(my_string, my_counter))
concatenated_string = lambda string, counter: string * counter
print(concatenated_string(my_string, my_counter))