import My_discounts
import My_orders


class Client:

    def __init__(self, name: str, order: My_orders.Order, discount: My_discounts.Discount):
        if not isinstance(name, str):
            raise TypeError('Name of client must be string')
        if not isinstance(order, My_orders.Order):
            raise TypeError('Wrong order data')
        if discount not in My_discounts.discounts:
            raise TypeError('Wrong discount data')
        self.name = name
        self.order = order
        self.discount = discount

    def count_order(self):
        temp = 0
        for dish, quantity in self.order.dishes_list.items():
            temp += dish.price * quantity
        return (temp - (temp / 100) * self.discount)
