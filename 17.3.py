from math import gcd

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        common = gcd(numerator, denominator)
        self.numerator = numerator // common
        self.denominator = denominator // common

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero.")
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    
    result_add = x + y
    result_sub = x - y
    result_mul = x * y
    result_div = x / y
    
    print(f"{x} + {y} = {result_add}")
    print(f"{x} - {y} = {result_sub}")
    print(f"{x} * {y} = {result_mul}")
    print(f"{x} / {y} = {result_div}")

    print(f"{x} == {y}: {x == y}")
    print(f"{x} == {result_add}: {x == result_add}")
