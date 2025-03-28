class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name}: {self.price} грн, наявність: {self.stock} шт"

class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity):
        if product.stock >= quantity:
            self.items.append((product, quantity))
            product.stock -= quantity
            print(f"{quantity} {product.name} додано в кошик.")
        else:
            print(f"Немає достатньо товару '{product.name}' в наявності.")

    def remove_product(self, product, quantity):
        for item in self.items:
            if item[0] == product:
                if item[1] >= quantity:
                    self.items.remove(item)
                    product.stock += quantity
                    print(f"{quantity} {product.name} видалено з кошика.")
                    return
                else:
                    print("В кошику немає такої кількості товару.")
                    return
        print(f"Товар {product.name} не знайдений у кошику.")

    def total_price(self):
        total = sum(item[0].price * item[1] for item in self.items)
        return total

    def checkout(self):
        total = self.total_price()
        print(f"Загальна вартість кошика: {total} грн")
        self.items.clear()
        print("Кошик очищено.")

    def show_cart(self):
        if not self.items:
            print("Кошик порожній.")
        else:
            for item in self.items:
                print(f"{item[1]} x {item[0].name} - {item[0].price * item[1]} грн")
            print(f"Загальна вартість: {self.total_price()} грн")



product1 = Product("Ноутбук", 15000, 5)
product2 = Product("Мишка", 400, 10)
product3 = Product("Клавіатура", 800, 3)

cart = Cart()

cart.add_product(product1, 2)
cart.add_product(product2, 1)
cart.add_product(product3, 1)

cart.show_cart()

cart.remove_product(product2, 1)

cart.show_cart()

cart.checkout()
