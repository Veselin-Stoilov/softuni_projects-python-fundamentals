import operator

data_cont = input()
contests_dict = {}
while data_cont != 'end of contests':
    contest = data_cont.split(':')[0]
    password = data_cont.split(':')[1]
    contests_dict[contest] = password

    data_cont = input()

data_user = input()
users_dict = {}
users_total_points = {}
while data_user != 'end of submissions':
    user_retake_same_contest = False
    contest_check = data_user.split('=>')[0]
    password_check = data_user.split('=>')[1]
    username = data_user.split('=>')[2]
    points = int(data_user.split('=>')[3])
    if contest_check in contests_dict and contests_dict[contest_check] == password_check:
        if username not in users_dict:
            users_dict[username] = []
            users_total_points[username] = 0
        for i in range(len(users_dict[username])):
            if users_dict[username][i][0] == contest_check:
                if points > users_dict[username][i][1]:
                    users_dict[username][i][1] = points
                user_retake_same_contest = True
        if user_retake_same_contest:
            data_user = input()
            continue
        else:
            users_dict[username].append((contest_check, points))  # adding (contest, points) for each user
            users_total_points[username] += points  # collecting total points for each user

    data_user = input()

for key, value in sorted(users_total_points.items(), key=lambda kvp: -kvp[1]):
    print(f"Best candidate is {key} with total {value} points.")
    print('Ranking:')
    break

# k = list(users_total_points.keys())
# v = list(users_total_points.values())
# print(f"{k[v.index(max(v))]}, {max(v)}")

# print(max(users_total_points.items(), key=operator.itemgetter(1)))

for name, contests in sorted(users_dict.items(), key=lambda kvp: kvp[0]):
    print(name)
    for i in sorted(contests, key=lambda x: -x[1]):  # name: [[js, 220], [python, 300], [c#, 250]]
        print(f'# {i[0]} -> {i[1]}')








