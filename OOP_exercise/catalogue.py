class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name):
        self.products.append(product_name)

    def __repr__(self):
        joined_str = '\n'.join(sorted(self.products))
        return f'Items in the {self.name} catalogue:\n' \
               f'{joined_str}'

    def get_by_letter(self, first_letter):
        get_by_letter_lst = [pr for pr in self.products if pr[0] == first_letter]
        return get_by_letter_lst


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)

