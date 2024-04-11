from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def make_a_payment(self):
        return NotImplementedError


class CreditCard(Payment):

    def make_a_payment(self):
        return "Payment was made by credit card"


class BankTransaction(Payment):

    def make_a_payment(self):
        return "Payment was made by bank transaction"


class WebMoney(Payment):

    def make_a_payment(self):
        return "Payment was made by WebMoney"


class PaymentProcessor:

    def __init__(self):
        self.payment_list = []

    def add_payment(self, payment):
        self.payment_list.append(payment)

    def process_payment(self, payment_method):
        if payment_method in self.payment_list:
            return payment_method.make_a_payment()
        else:
            return "Payment method not available"


credit_card = CreditCard()
bank_transaction = BankTransaction()
web_money = WebMoney()

payment_processor = PaymentProcessor()

payment_processor.add_payment(credit_card)
payment_processor.add_payment(bank_transaction)
payment_processor.add_payment(web_money)

payment1 = payment_processor.process_payment(credit_card)
print(payment1)

payment2 = payment_processor.process_payment(bank_transaction)
print(payment2)

payment3 = payment_processor.process_payment(web_money)
print(payment3)
