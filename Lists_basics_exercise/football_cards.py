red_cards = input()
red_cards_list = red_cards.split()
red_cards_list = set(red_cards_list)
is_terminated = False
players_a_counter = 11
players_b_counter = 11
team_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
for red_card in red_cards_list:
    red_card_list = red_card.split('-')
    if red_card_list[0] == 'A':
        red_card_list[1] = int(red_card_list[1])
        team_a.remove(red_card_list[1])
        players_a_counter -= 1
        if players_a_counter < 7:
            is_terminated = True
            break
    if red_card_list[0] == 'B':
        red_card_list[1] = int(red_card_list[1])
        team_b.remove(red_card_list[1])
        players_b_counter -= 1
        if players_b_counter < 7:
            is_terminated = True
            break

print(f'Team A - {players_a_counter}; Team B - {players_b_counter}')
if is_terminated:
    print('Game was terminated')