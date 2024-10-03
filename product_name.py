class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity
    
product1 = Product("Laptop", 1000, 5)
print(f"Total value of {product1.name}: ${product1.total_value()}")