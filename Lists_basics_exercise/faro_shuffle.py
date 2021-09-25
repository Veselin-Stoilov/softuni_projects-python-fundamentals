cards_str = input()
shuffle_times = int(input())
index_counter = 0
cards_list = cards_str.split()
first_half = cards_list[0:(int(len(cards_list)/2))]
second_half = cards_list[(int(len(cards_list)/2)):]
for shuffle in range(shuffle_times):
    for swap in range(0, len(first_half-1)):
        second_half[swap] = first_half[swap + 1]
        second_half[swap + 1] = second_half[swap]
        first_half[0] = first_half[0]
        first_half[1] =
        cards_list[0] >> cards_list[0]
        cards_list[1],cards_list[2] >> cards_list[2],cards_list[4] #swap, swap*2
        cards_list[2],cards_list[4] >> cards_list[4],cards_list
        cards_list[3] >> cards_list[6]
        cards_list[swap*2],cards_list[4] = cards_list[swap], cards_list[2]

    cards_list = first_half + second_half

print(first_half)
print(second_half)



