def loading_bar(percentage):
    loading_len = ['.']*10
    for num in range(0, percentage_loaded//10):
        loading_len[num] = '%'
    if percentage == 100:
        print('100% Complete!')
        print(f'[{"".join(loading_len)}]')
    else:
        print(f'{percentage_loaded}% [{"".join(loading_len)}]')
        print('Still loading...')


percentage_loaded = int(input())
loading_bar(percentage_loaded)