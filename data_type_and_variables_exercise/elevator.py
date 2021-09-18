num_of_people = int(input())
elevator_capacity = int(input())

courses = num_of_people // elevator_capacity
if num_of_people % elevator_capacity != 0:
    courses += 1
print(courses)
