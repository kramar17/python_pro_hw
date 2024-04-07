class BalanceDescriptor:

    def __init__(self):
        self.balance = 0


class BankAccount:

    def __init__(self):
        self.__balance = BalanceDescriptor()

    

