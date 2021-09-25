def perfect_number(number: int):
    aliquot_sum = 0
    for num in range(1, number):
        if number % num == 0:
            aliquot_sum += num
    if number == aliquot_sum:
        print('We have a perfect number!')
    else:
        print("It's not so perfect.")


given_num = int(input())
perfect_number(given_num)