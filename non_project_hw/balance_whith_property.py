class BalanceDescriptor:
    def __get__(self, instance, owner):
        return instance._balance

    def __set__(self, instance, value):
        raise AttributeError("You can't change balance directly")


class BankAccount:
    balance = BalanceDescriptor()

    def __init__(self, initial_balance=0):
        self._balance = initial_balance

    def __setattr__(self, key, value):
        if key == "_balance":
            object.__setattr__(self, key, value)
        else:
            print("You can't change balance")

    def __getattr__(self, item):
        return "wrong attribute"


test_account = BankAccount()
print(test_account.balance)
test_account.balance = 100
print(test_account.balance)
print(test_account.istory)
