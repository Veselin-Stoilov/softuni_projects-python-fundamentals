def chairs_availability(seats, guests, room):
    chairs_difference = abs(seats - guests)
    if seats < guests:
        print(f'{chairs_difference} more chairs needed in room {room}')


def extra_chairs(seats: int, guests: int):
    if seats > guests:
        additional_chairs = seats - guests
        return additional_chairs
    else:
        return 0


def room_needs_chairs(seats, guests):
    if seats < guests:
        return True


rooms = int(input())
total_extra_chairs = 0
room_not_ready = 0
for room in range(1, rooms + 1):
    chairs_vs_pax = input().split(' ')
    room_num = room
    chairs = len(chairs_vs_pax[0])
    pax = int(chairs_vs_pax[1])
    chairs_availability(chairs, pax, room_num)
    total_extra_chairs += int(extra_chairs(chairs, pax))
    if room_needs_chairs(chairs, pax):
        room_not_ready += 1
        continue
if room_not_ready == 0:
    print(f'Game On, {total_extra_chairs} free chairs left')