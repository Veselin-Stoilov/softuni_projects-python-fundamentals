command = input()
course_info = {}
while command != 'end':
    command = command.split(' : ')
    course = command[0]
    student = command[1]
    if course not in course_info:
        course_info[course] = [student]
    else:
        course_info[course].append(student)
    command = input()
for key in course_info.keys():
    course_info[key].sort()
for course in sorted(course_info, key=lambda kvp: len(course_info[kvp]), reverse=True):
    print(f'{course}: {len(course_info[course])}')
    for name in course_info[course]:
        print(f'-- {name}')
