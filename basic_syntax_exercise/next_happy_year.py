year = int(input())
while True:
    year = year + 1
    year = str(year)
    if len(set(year)) == len(year):
        print(year)
        break
    else:
        year = int(year)
        continue