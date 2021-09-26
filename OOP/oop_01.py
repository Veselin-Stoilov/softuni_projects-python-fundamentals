class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed # instances attributes: speed and mileage
        self.mileage = mileage


modelX = Vehicle(220, 400)
print('ModelX specs:', modelX.max_speed, modelX.mileage)
