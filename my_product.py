class Product:

    def __init__(self, name: str, description: str, price: int | float):
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f'{self.name}, {self.description}, price: {self.price} UAH'


