# Q10: Calculate product total cost from price and quantity.
class Product:
    def total_cost(self, price, quantity):
        return price * quantity

product = Product()
print(product.total_cost(100, 3))
