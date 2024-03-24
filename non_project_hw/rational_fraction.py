import math


class RationalFraction:

    def __init__(self, up: int, down: int):
        if not isinstance(up, int):
            raise TypeError("Numerator must be a integer number")
        if not isinstance(down, int):
            raise TypeError("Denominator must be a integer number")
        if down == 0:
            raise ZeroDivisionError("Denominator must not be a zero")
        if down < 0:
            raise ValueError("Denominator must be positive")
        self.up = up
        self.down = down

    def __str__(self):
        if self.up == self.down:
            return "1"
        if self.up == 0:
            return "0"
        temp = math.gcd(self.up, self.down)
        return f'{int(self.up/temp)}/{int(self.down/temp)}'

    def __add__(self, other):
        new_down = self.down * other.down
        new_up = (self.up * other.down) + (other.up * self.down)
        return RationalFraction(new_up, new_down)

    def __sub__(self, other):
        new_down = self.down * other.down
        new_up = (self.up * other.down) - (other.up * self.down)
        if new_up == 0:
            return 0
        return RationalFraction(new_up, new_down)

    def __mul__(self, other):
        new_down = self.down * other.down
        new_up = self.up * other.up
        return RationalFraction(new_up, new_down)

    def __lt__(self, other):
        return (self.up * other.down) < (other.up * self.down)

    def __gt__(self, other):
        return (self.up * other.down) > (other.up * self.down)

    def __eq__(self, other):
        return (self.up * other.down) == (other.up * self.down)

    def __le__(self, other):
        return (self.up * other.down) <= (other.up * self.down)

    def __ge__(self, other):
        return (self.up * other.down) >= (other.up * self.down)

    def __ne__(self, other):
        return (self.up * other.down) != (other.up * self.down)


test1 = RationalFraction(-9, 4)
test2 = RationalFraction(2, 4)

print(test1 + test2)

