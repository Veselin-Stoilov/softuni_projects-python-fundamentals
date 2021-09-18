stud_data = input()
stud_info_dict = {}
students_in_same_class = []
while ':' in stud_data:
    stud_data = stud_data.split(':')
    name, id_num, course_name = stud_data[0], stud_data[1], stud_data[2]
    students_in_same_class = []
    student_name_and_id = [name, id_num]
    if course_name not in stud_info_dict:
        stud_info_dict[course_name] = students_in_same_class
    stud_info_dict[course_name].append(student_name_and_id)
    stud_data = input()
stud_data = ' '.join(stud_data.split('_'))
for key, value in stud_info_dict.items():
    if key == stud_data:
        for el in stud_info_dict[stud_data]:
            print(f"{' - '.join(el)}")



