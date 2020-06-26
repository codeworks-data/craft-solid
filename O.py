# Open-closed principle


class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def get_discount_price(self):
        if self.customer == 'fav':
            return self.price * 0.2
        if self.customer == 'vip':
            return self.price * 0.5
        return self.price
