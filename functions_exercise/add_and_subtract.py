def add_and_subtract(n_1, n_2, n_3):

    def sum_numbers(n_1, n_2):
        return n_1 + n_2

    def subtract(sum, n_3):
        return sum - n_3

    return subtract(sum_numbers(n_1, n_2), n_3)


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

print(add_and_subtract(num_1, num_2, num_3))
