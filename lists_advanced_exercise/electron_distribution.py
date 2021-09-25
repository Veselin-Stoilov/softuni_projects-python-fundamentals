def electrons_distribution(electrons_count):
    electrons_left = electrons
    shell_position = 1
    filled_shells_list = []
    while electrons_left > 0:
        max_electrons_in_shell = 2 * shell_position ** 2
        if max_electrons_in_shell <= electrons_left:
            filled_shells_list.append(max_electrons_in_shell)
            electrons_left -= max_electrons_in_shell
        else:
            filled_shells_list.append(electrons_left)
            electrons_left = 0
        shell_position += 1
    return filled_shells_list


electrons = int(input())
print(electrons_distribution(electrons))
