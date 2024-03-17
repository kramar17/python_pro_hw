import my_discounts
import my_orders


class Client:

    def __init__(self, name: str, order: my_orders.Order, discount: my_discounts.Discount):
        if not isinstance(name, str):
            raise TypeError('Name of client must be string')
        if not isinstance(order, my_orders.Order):
            raise TypeError('Wrong order data')
        if discount not in my_discounts.discounts:
            raise TypeError('Wrong discount data')
        self.name = name
        self.order = order
        self.discount = discount

    def count_order(self):
        temp = 0
        for dish, quantity in self.order.dishes_list.items():
            temp += dish.price * quantity
        return (temp - (temp / 100) * self.discount)
