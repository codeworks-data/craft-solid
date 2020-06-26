# Open-closed principle


class DiscountCustomer:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def get_discount_price(self):
        return self.price


class FavoriteDiscountCustomer(DiscountCustomer):
    def get_discount_price(self):
        return super().get_discount_price() * 0.8  # 20% discount


class VIPDiscountCustomer(DiscountCustomer):
    def get_discount_price(self):
        return super().get_discount_price() * 0.5

