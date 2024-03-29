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

    def __len__(self):
        return MenuIterator.get_len(self.dishes)

    def __getitem__(self, index):
        if isinstance(index, int):
            return MenuIterator.get_item(self.dishes, index)
        if isinstance(index, slice):
            return MenuIterator.getitem_slice(self.dishes, index, 'dish')

    def __iter__(self):
        return MenuIterator(self.dishes)


class Menu:

    def __init__(self, name):
        self.name = name
        self.category_list = []

    def add_category(self, category: MenuCategory):
        self.category_list.append(category)

    def __str__(self):
        return ''.join(map((lambda x: str(x) + '\n'), self.category_list))
    
    def __len__(self):
        return MenuIterator.get_len(self.category_list)

    def __getitem__(self, index):
        if isinstance(index, int):
            return MenuIterator.get_item(self.category_list, index)
        if isinstance(index, slice):
            return MenuIterator.getitem_slice(self.category_list, index, 'category')

    def __iter__(self):
        return MenuIterator(self.category_list)
        

class MenuIterator:

    def __init__(self, some_list):
        self.items = some_list
        self.index = 0

    def __next__(self):
        if self.index < len(self.items):
            result = self.items[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

    def __iter__(self):
        self.index = 0
        return self

    @staticmethod
    def get_len(some_list):
        return len(some_list)

    @staticmethod
    def get_item(some_list, index):
        return some_list[index]

    @staticmethod
    def getitem_slice(some_list, index, item):
        start = index.start or 0
        stop = index.stop or len(some_list)
        step = index.step or 1

        if item == 'dish':
            result = MenuCategory(f'slice [{start}:{stop}:{step}]')
            for i in range(start, stop, step):
                result.add_dish(some_list[i])
            return result

        if item == 'category':
            result = Menu(f'slice [{start}:{stop}:{step}]')
            for i in range(start, stop, step):
                result.add_category(some_list[i])
            return result


