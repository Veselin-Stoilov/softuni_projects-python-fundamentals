class Vehicle:
    def __init__(self, type, model, price, owner=None):
        self.type = type
        self.model = model
        self.price = price
        self.owner = owner

    def buy(self, money, owner):
        if money >= self.price:
            if self.owner is None:
                self.owner = owner
                change = money - self.price
                change = round(change, 2)
                output = f"Successfully bought a {self.type}. Change: {change}"
                return output
            else:
                output = "Car already sold"
                return output
        elif money < self.price:
            output = "Sorry not enough money"
            return output

    def sell(self):
        if self.owner is not None:
            self.owner = None
        else:
            output = "Vehicle has no owner"
            return output

    def __repr__(self):
        if self.owner is not None:
            output = f"{self.model} {self.type} is owned by: {self.owner}"
            return output
        else:
            output = f"{self.model} {self.type} is on sale: {self.price}"
            return output


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)


