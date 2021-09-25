def factorial_division(num_1, num_2):
    num_1_fact = num_1
    num_2_fact = num_2
    for num in range(num_1 - 1, num_2, -1):
        num_1_fact *= num
    return f'{num_1_fact:.2f}'


n_1 = int(input())
n_2 = int(input())
print(factorial_division(n_1, n_2))