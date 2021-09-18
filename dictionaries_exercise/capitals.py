countries = input().split(', ')
capitals = input().split(', ')
countries_capitals = dict(zip(countries, capitals))
for country, capital in countries_capitals.items():
    print(f'{country} -> {capital}')
