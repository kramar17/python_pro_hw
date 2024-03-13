import My_menu
import My_logger


class Order:
    __next_order_num = 1

    def __init__(self):
        self.__order_num = Order.__next_order_num
        Order.__next_order_num += 1
        self.dishes_list = {}
        My_logger.logger.info(f'New order was created. Number: {self.__order_num}')

    def add_to_order(self, dish: My_menu.Dish, quantity: int):
        if not isinstance(dish, My_menu.Dish):
            raise TypeError("Only dishes can be added to order")
        if not isinstance(quantity, int):
            raise TypeError('Quantity of dishes must be a number')
        if dish in self.dishes_list.keys():
            self.dishes_list[dish] += quantity
        else:
            self.dishes_list[dish] = quantity

    def remove_from_order(self, dish: My_menu.Dish, quantity: int):
        if not isinstance(dish, My_menu.Dish):
            raise TypeError('Wrong type of object. muct be Dish')
        if not isinstance(quantity, int):
            raise TypeError('Quantity must be intteger number')
        if self.dishes_list[dish] <= quantity:
            del self.dishes_list[dish]
        else:
            self.dishes_list[dish] -= quantity

    def __str__(self):
        return ''.join(
            map(lambda x: x[0].name + " x " + str(x[1]) + ' cost ' + str(x[0].price) + '\n', self.dishes_list.items()))
