class Order:
    def __init__(self,product,price):
        self.product = product
        self.price = price
        print(f"The price of {self.product} is {self.price}")

    def __gt__(self,order2):
        return self.price > order2.price

order1 = Order("Chips",20)
order2 = Order("Ice Cream",60)

if (order2>order1):
    print("Order2 > Order1")
else:
    print("Order2 < Order1")