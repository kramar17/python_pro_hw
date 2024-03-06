class PriceError(Exception):

    def __init__(self, messege: str) -> None:
        self.messege = messege
        super().__init__(messege)

    def __str__(self) -> str:
        return f'Price must be above zero {self.messege}'
