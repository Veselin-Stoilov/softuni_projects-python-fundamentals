command = input()
exams_info = {}
language_list = []
banned_students = []
while command != 'exam finished':
    command = command.split('-')
    user = command[0]
    if len(command) == 2:
        if command[1] == 'banned':
            banned_students.append(user)
    elif len(command) == 3:
        language = command[1]
        points = int(command[2])
        language_list.append(language)
        if user not in exams_info:
            exams_info[user] = [(language, points)]
        else:
            exams_info[user].append((language, points))
    command = input()
for user, result in exams_info.items():
    result.sort(key=lambda x: -x[1])
print('Results:')
for user, exam in sorted(exams_info.items(), key=lambda kvp: (-kvp[1][0][1], kvp)):
    if user not in banned_students:
        highest_score = exam[0][1]
        print(f'{user} | {highest_score}')
print('Submissions:')
for language in sorted(list(set(language_list))):
    print(f'{language} - {language_list.count(language)}')