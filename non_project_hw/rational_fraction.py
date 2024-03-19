import math


class RationalFraction:

    def __init__(self, up: int, down: int):
        if down == 0:
            raise ZeroDivisionError("Denominator must not be a zero")
        if not isinstance(up, int):
            raise TypeError("Numerator must be a integer number")
        if not isinstance(down, int):
            raise TypeError("Denominator must be a integer number")
        if down < 0:
            raise ValueError("Denominator must be positive")
        self.up = up
        self.down = down

    def __str__(self):
        if self.up == self.down:
            return "1"
        return f'{self.up}/{self.down}'

    def __add__(self, other):
        new_down = self.down * other.down
        new_up = (self.up * other.down) + (other.up * self.down)
        temp = math.gcd(new_up, new_down)
        return RationalFraction(int(new_up/temp), int(new_down/temp))

    def __sub__(self, other):
        new_down = self.down * other.down
        new_up = (self.up * other.down) - (other.up * self.down)
        temp = math.gcd(new_up, new_down)
        if new_up == 0:
            return 0
        return RationalFraction(int(new_up / temp), int(new_down / temp))

    def __mul__(self, other):
        new_down = self.down * other.down
        new_up = self.up * other.up
        temp = math.gcd(new_up, new_down)
        return RationalFraction(int(new_up / temp), int(new_down / temp))

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

