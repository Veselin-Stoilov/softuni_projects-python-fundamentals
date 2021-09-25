def odd_even_sum(number_str):
    even_sum = 0
    odd_sum = 0
    for el in number_str:
        num = int(el)
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'


num = input()
print(odd_even_sum(num))