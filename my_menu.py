import my_exeptions
import my_logger


class Dish:

    def __init__(self, name: str, description: str, price: int):
        if not isinstance(name, str):
            raise TypeError('Name must be a string')
        if not isinstance(description, str):
            raise TypeError('Description must be a string')
        if not isinstance(price, (int, float)):
            raise TypeError('Price must be a number')
        if price <= 0:
            raise my_exeptions.PriceError('Wrong price')
        self.name = name
        self.description = description
        self.price = price
        my_logger.logger.info(f'New dish was created. Name: {self.name}')

    def __str__(self):
        return f"{self.name} is a {self.description} cost {self.price} dollars"


class MenuCategory:

    def __init__(self, name, *dishes):
        if not isinstance(name, str):
            raise TypeError("Name ust be a string")
        for i in dishes:
            if not isinstance(i, Dish):
                raise ValueError(" Only dishes can be added in menu category")
        self.name = name
        self.dishes = list(dishes)
        my_logger.logger.info(f'New menu category was created. Name: {self.name}')

    def add_dish(self, dish: Dish):
        if dish not in self.dishes:
            self.dishes.append(dish)

    def remove_dish(self, dish):
        if dish in self.dishes:
            self.dishes.remove(dish)

    def __str__(self):
        return f'{self.name}:\n {", ".join(str(dish.name) for dish in self.dishes)}\n'


class Menu:

    def __init__(self, name):
        self.name = name
        self.category_list = []

    def add_category(self, category: MenuCategory):
        self.category_list.append(category)

    def __str__(self):
        return ''.join(map((lambda x: str(x) + '\n'), self.category_list))
