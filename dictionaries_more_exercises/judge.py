line = input()
contests_dict = {}
individual_standings = {}

while line != 'no more time':
    user_retake_same_contest = False
    username = line.split(' -> ')[0]
    contest = line.split(' -> ')[1]
    points = int(line.split(' -> ')[2])
    if contest not in contests_dict:
        contests_dict[contest] = []
    for i in range(len(contests_dict[contest])):
        if contests_dict[contest][i][0] == username:
            if contests_dict[contest][i][1] < points:
                contests_dict[contest][i][1] = points
                individual_standings[username] = points
            user_retake_same_contest = True
    if not user_retake_same_contest:
        contests_dict[contest].append([username, points])
        if username not in individual_standings:
            individual_standings[username] = 0
        individual_standings[username] += points

    line = input()

for contest_name, participants in contests_dict.items():
    participants_count = len(participants)
    print(f'{contest_name}: {participants_count} participants')
    position = 1
    for participant in sorted(participants, key=lambda x: (-x[1])):
        user = participant[0]
        user_points = participant[1]
        print(f'{position}. {user} <::> {user_points}')
        position += 1

print("Individual standings:")
position_counter = 1
for user, points in sorted(individual_standings.items(), key=lambda kvp: (-kvp[1], kvp[0])):
    print(f"{position_counter}. {user} -> {points}")
    position_counter += 1
