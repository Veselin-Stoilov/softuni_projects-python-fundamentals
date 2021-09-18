snowballs_number = int(input())
import sys
snowball_value_max = -sys.maxsize
for snowball in range(1, snowballs_number + 1):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_snow / snowball_time) ** snowball_quality
    if snowball_value > snowball_value_max:
        snowball_value_max = int(snowball_value)
        snowball_snow_best = snowball_snow
        snowball_time_best = snowball_time
        snowball_quality_best = snowball_quality
print(f'{snowball_snow_best} : {snowball_time_best} = {snowball_value_max} ({snowball_quality_best})')