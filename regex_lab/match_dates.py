text = input()
import re
pattern = r'\b(?P<day>[0-9]{2})(?P<separator>(-|/|\.))(?P<month>[A-Z][a-z]{2})(?P=separator)(?P<year>[0-9]{4})\b'
valid_dates = re.finditer(pattern, text)
for date in valid_dates:
    current_date = date.groupdict()
    print(f"Day: {current_date['day']}, Month: {current_date['month']}, Year: {current_date['year']}")