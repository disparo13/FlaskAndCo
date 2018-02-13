class Store:
    def __init__(self, name):
        self.name = name
        self.items = []
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.

    def add_item(self, name, price):
        self.items.append({'name': name, 'price': price})
        # Create a dictionary with keys name and price, and append that to self.items.

    def stock_price(self):
        return sum([ item['price'] for item in self.items])
        # total = 0
        # for item in self.items:
        #     total += item['price']
        # return(total)
        # Add together all item prices in self.items and return the total.

ramStore = Store('Ramstore')

ramStore.add_item('Huita', 22)
ramStore.add_item('Pizdota', 56)

print(ramStore.items)
print(ramStore.stock_price())

