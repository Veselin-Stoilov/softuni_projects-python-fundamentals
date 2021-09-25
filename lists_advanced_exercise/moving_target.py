def shoot_range_check(targets, cmd_index):
    if cmd_index in range(0, len(targets)):
        return True
    else:
        return False


def add_range_check(targets, cmd_index):
    """ returns False if index out of range """
    if cmd_index in range(0, len(targets)):
        return True
    else:
        return False


def strike_range_check(targets, strike_left_range, strike_right_range):
    if strike_left_range in range(0, len(targets)) \
            or strike_right_range in range(0, len(targets)):
        return True
    else:
        return False


def shoot_targets(targets, cmd_index, cmd_value):
    targets[cmd_index] -= cmd_value
    if targets[cmd_index] <= 0:
        targets.pop(cmd_index)
    return targets


def add_target(targets, cmd_index, cmd_value):
    targets.insert(cmd_index, cmd_value)
    return targets


def strike_target(targets, strike_left_range, strike_right_range):
    del targets[strike_left_range: strike_right_range + 1]
    return targets


targets = input().split(' ')
targets = [int(x) for x in targets]
cmd = input()
while cmd != 'End':
    cmd = cmd.split(' ')
    cmd_type = cmd[0]
    cmd_index = int(cmd[1])
    cmd_value = int(cmd[2])
    if cmd_type == 'Shoot':
        if not shoot_range_check(targets, cmd_index):
            cmd = input()
            continue
        else:
            targets = shoot_targets(targets, cmd_index, cmd_value)
    elif cmd_type == 'Add':
        if not add_range_check(targets, cmd_index):
            print('Invalid placement!')
        else:
            targets = add_target(targets, cmd_index, cmd_value)
    elif cmd_type == 'Strike':
        strike_left_range = cmd_index - cmd_value
        strike_right_range = cmd_index + cmd_value
        if not strike_range_check(targets, strike_left_range, strike_right_range):
            print('Strike missed!')
        else:
            targets = strike_target(targets, strike_left_range, strike_right_range)
    cmd = input()
targets = [str(x) for x in targets]
targets = '|'.join(targets)
print(targets)


