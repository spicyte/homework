class Product:
    def __init__(self, product_type, name, price):
        self.type = product_type
        self.name = name
        self.price = price

class ProductStore:
    def __init__(self):
        self.products = {}
        self.income = 0

    def add(self, product, amount):
        if product.name not in self.products:
            self.products[product.name] = {'type': product.type, 'price': product.price * 1.3, 'amount': 0}
        self.products[product.name]['amount'] += amount

    def set_discount(self, identifier, percent, identifier_type='name'):
        for product_name, product_info in self.products.items():
            if identifier_type == 'name' and product_name == identifier:
                product_info['price'] *= (100 - percent) / 100
            elif identifier_type == 'type' and product_info['type'] == identifier:
                product_info['price'] *= (100 - percent) / 100

    def sell_product(self, product_name, amount):
        if product_name not in self.products or self.products[product_name]['amount'] < amount:
            raise ValueError(f"Cannot sell {amount} units of {product_name}. Insufficient stock.")
        else:
            self.products[product_name]['amount'] -= amount
            self.income += amount * self.products[product_name]['price']

    def get_income(self):
        return self.income

    def get_all_products(self):
        return self.products

    def get_product_info(self, product_name):
        if product_name in self.products:
            product_info = self.products[product_name]
            return product_info['name'], product_info['amount']
        else:
            raise ValueError(f"Product {product_name} not found in the store.")


p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)
s = ProductStore()

s.add(p, 10)
s.add(p2, 300)

s.sell_product('Ramen', 10)

assert s.get_product_info('Ramen') == ('Ramen', 290)






