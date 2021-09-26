class Inventory:
    def __init__(self, __capacity):
        self.items = []
        self.capacity = __capacity

    def add_item(self, item):
        if len(self.items) < self.capacity:
            self.items.append(item)
        else:
            output = "not enough room in the inventory"
            return output

    def get_capacity(self):
        return self.capacity

    def __repr__(self):
        left_capacity = self.capacity - len(self.items)
        output = f"Items {', '.join(self.items)}.\nCapacity left: {left_capacity}"
        return output


inventory = Inventory(2)
inventory.add_item("potion")
inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)

print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)

