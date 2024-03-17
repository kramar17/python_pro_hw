class PriceError(Exception):

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)

    def __str__(self) -> str:
        return f'Price must be above zero {self.message}'


class QuantityError(Exception):

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)

    def __str__(self) -> str:
        return f'Quantity must be above zero {self. meggage}'


class RemoveError(Exception):

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)

    def __str__(self) -> str:
        return f'You dont have this product in your cart {self. meggage}'