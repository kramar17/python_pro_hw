class Product:

    def __init__(self, name: str, description: str, price: int | float):
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f'{self.name}\n{self.description} \nprice: {self.price} UAH'


