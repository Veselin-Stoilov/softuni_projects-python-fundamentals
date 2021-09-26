class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Buss(Vehicle):
    pass


school_bus = Buss('Volvo', 140, 200)
print(f'School bus is {school_bus.name}, maximum speed: {school_bus.max_speed} and mileage of {school_bus.mileage}')

