import my_product
import my_exeptions


class ProductCart:

    def __init__(self, name: str):
        self.name = name
        self.product_list = {}
        self.iter_list = []

    def add_product(self, product: my_product, quantity: int | float):
        if quantity <= 0:
            raise my_exeptions.PriceError
        if product in self.product_list.keys():
            self.product_list[product] += quantity
        else:
            self.product_list[product] = quantity
            self.iter_list.append(product)

    def remove_from_cart(self, product: my_product.Product, quantity: int|float = None):
        if not isinstance(product, my_product.Product) and isinstance(quantity, int | float) or quantity is None:
            raise ValueError('You can only delete some product from cart. Quantity must be a number')
        if quantity <= 0:
            raise my_exeptions.QuantityError
        if product not in self.product_list.keys():
            raise my_exeptions.RemoveError('try another product')
        if quantity is None:
            del self.product_list[product]
            self.iter_list.remove(product)
        else:
            self.product_list[product] -= quantity
        if quantity:
            self.product_list[product] -= quantity
        if self.product_list[product] - quantity <= 0:
            del self.product_list[product]
            self.iter_list.remove(product)

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
        result_cart.iter_list = list(set(self.iter_list) | set(other.iter_list))
        return result_cart

    def __str__(self):
        product_quantities = [f"{product.name}: {quantity}" for product, quantity in self.product_list.items()]
        return f"Cart name: {self.name}\n" + "\n".join(product_quantities)

    def __getitem_slice(self, index):
        start = index.start or 0
        stop = index.stop or len(self.iter_list) + 1
        step = index.step or 1
        result = ProductCart(f'{self.name} slice [{start}:{stop}:{step}]')
        for i in self.iter_list[start:stop:step]:
            result.add_product(i, self.product_list[i])
        return result

    def __getitem__(self, item):
        if not isinstance(item, int | slice):
            raise ValueError("Index must be a integer number or slice")
        if isinstance(item, int):
            if item > len(self.iter_list)-1:
                raise IndexError("Out of range")
            return str(self.iter_list[item]), self.product_list[self.iter_list[item]]
        if isinstance(item, slice):
            return self.__getitem_slice(item)


try:
    product_1 = my_product.Product('fish', 'salmon file', 10)
    product_2 = my_product.Product('meat', 'beef file', 20)
    product_3 = my_product.Product('carrot', 'fresh carrot', 5)
    product_4 = my_product.Product('bread', 'white bread', 6)
    cart_1 = ProductCart('My cart')
    cart_1.add_product(product_1, 1)
    cart_1.add_product(product_2, 2)
    cart_1.add_product(product_3, 1)
    cart_1.add_product(product_4, 1)
    print(cart_1)
    print(cart_1.count_price())
except (TypeError, ValueError, my_exeptions.PriceError, my_exeptions.RemoveError, my_exeptions.QuantityError) as e:
    print(e)

print(cart_1[1:3])