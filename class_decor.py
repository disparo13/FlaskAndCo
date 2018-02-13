class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        newname = store.name + " - franchise"
        return Store(newname)
        # Return another store, with the same name as the argument's name, plus " - franchise"

    @staticmethod
    def store_details(store):
        #return store.name + ", total stock price: " + str(store.stock_price())
        return '{0}, total stock price: {1}'.format(store.name, store.stock_price())
    # Return a string representing the argument
    # It should be in the format 'NAME, total stock price: TOTAL'

store = Store("Test")
store2 = Store("Amazon")
store2.add_item("Keyboard", 160)

store3 = Store.franchise(store)
print(store3.name)

print(Store.store_details(store))
print(Store.store_details(store2))
