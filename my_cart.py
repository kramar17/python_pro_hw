import my_product
import my_exeptions


class ProductCart:


    def __init__(self, name: str):
        self.name = name
        self.product_list = {}

    def add_product(self, product: my_product, quantity: int|float):
        if quantity <= 0:
            raise my_exeptions.PriceError
        if product in self.product_list.keys():
            self.product_list[product] += quantity
        else:
            self.product_list[product] = quantity

    def remove_from_cart(self, product: my_product.Product, quantity: int|float = None):
        if not isinstance(product, my_product.Product) and isinstance(quantity, int | float) or quantity is None:
            raise ValueError('You can only delete some product from cart. Quantity must be a number')
        if quantity <= 0:
            raise my_exeptions.QuantityError
        if product not in self.product_list.keys():
            raise my_exeptions.RemoveError('try another product')
        if quantity is None:
            del self.product_list[product]
        else:
            self.product_list[product] -= quantity

        if quantity:
            self.product_list[product] -= quantity
        else:
            del self.product_list[product]

    def count_price(self):
        return sum(product.price * quantity for product, quantity in self.product_list.items())

    def __add__(self, other):
        if not isinstance(other, ProductCart):
            raise ValueError(' You can only add cart to cart')

        result_cart = ProductCart(f'{self.name}_+_{other.name}')
        result_cart.product_list = self.product_list.copy()
        for product, value in other.product_list.items():
            if product in result_cart.product_list.keys():
                result_cart.product_list[product] += value
            else:
                result_cart.product_list[product] = value
        return result_cart


    def __str__(self):
        product_quantities = [f"{product.name}: {quantity}" for product, quantity in self.product_list.items()]
        return f"Cart name: {self.name}\n" + "\n".join(product_quantities)


try:
    product_1 = my_product.Product('fish', 'file', 10)
    product_2 = my_product.Product('meat', 'file', 20)
    cart_1 = ProductCart('My cart')
    cart_1.add_product(product_1, 2)
    cart_1.add_product(product_2, 1)
    cart_1.remove_from_cart(product_1, 1)
    print(cart_1)
    print(cart_1.count_prise())
except (TypeError, ValueError, my_exeptions.PriceError, my_exeptions.RemoveError, my_exeptions.QuantityError) as e:
    print(e)