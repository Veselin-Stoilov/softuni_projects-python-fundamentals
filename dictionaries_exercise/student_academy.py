n = int(input())
students_dict = {}
top_students_dict = {}
students_list= []
for _ in range(n * 2):
    name_grade = input()
    students_list.append(name_grade)
for i in range(0, len(students_list), 2):
    name = students_list[i]
    grade = float(students_list[i + 1])
    if name not in students_dict:
        students_dict[name] = [grade]
    else:
        students_dict[name].append(grade)
for student, grade in students_dict.items():
    average_grade = sum(grade)/len(grade)
    if average_grade >= 4.50:
        top_students_dict[student] = average_grade
for student, grade in sorted(top_students_dict.items(), key=lambda grade: grade, reverse=True):
    print(f'{student} -> {grade:.2f}')