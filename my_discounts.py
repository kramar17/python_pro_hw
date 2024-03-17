class Discount:
    @classmethod
    def discount(cls):
        return 0


class RegularDiscount(Discount):
    @classmethod
    def discount(cls):
        return 5


class SilverDiscount(Discount):
    @classmethod
    def discount(cls):
        return 7


class GoldDiscount(Discount):
    @classmethod
    def discount(cls):
        return 10



discount = Discount.discount()
regular_discount = RegularDiscount.discount()
silver_discount = SilverDiscount.discount()
gold_discount = GoldDiscount.discount()

discounts = [discount, regular_discount, silver_discount, gold_discount]