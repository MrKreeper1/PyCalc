from math import *


class Number_old:
    numer, denom, val = 1, 1, 1
    def __init__(self, numer, denom = 1):
        self.repl()
        self.numer = numer
        self.denom = denom
        self.val = numer / denom

    def repl(self):
        assert isinstance(self.numer, (int, float, complex))
        assert isinstance(self.denom, (int, float, complex))
        assert self.denom != 0
        self.val = self.numer / self.denom
        
        if isinstance(self.numer, complex) and not self.numer.imag:
            self.numer = self.numer.real
        if isinstance(self.denom, complex) and not self.denom.imag:
            self.denom = self.denom.real

        if isinstance(self.numer, float) and self.numer == int(self.numer):
            self.numer = int(self.numer)
        if isinstance(self.denom, float) and self.denom == int(self.denom):
            self.denom = int(self.denom)
        
        if isinstance(self.val, (int, float)) and self.numer / self.denom == self.numer // self.denom:
            self.val = int(self.val)


    def __repr__(self):
        self.repl()
        return str(self.val)

    def __str__(self):
        self.repl()
        return self.__repr__()

    def __lt__(self, other):
        self.repl()
        return self.val < other

    def __le__(self, other):
        self.repl()
        return self.val <= other

    def __eq__(self, other):
        self.repl()
        return self.val == other

    def __ne__(self, other):
        self.repl()
        return self.val != other
    
    def __gt__(self, other):
        self.repl()
        return self.val > other

    def __ge__(self, other):
        self.repl()
        return self.val >= other

    def __bool__(self):
        self.repl()
        return self.val != 0

    def __add__(self, other):
        self.repl()
        return Number_old(self.val + other)

    def __sub__(self, other):
        self.repl()
        return Number_old(self.val - other)

    def __mul__(self, other):
        self.repl()
        return Number_old(self.val * other)

    def __truediv__(self, other):
        self.repl()
        return Number_old(self.numer, self.denom * other)

    def __floordiv__(self, other):
        self.repl()
        return Number_old(self.val // other)

    def __mod__(self, other):
        self.repl()
        return Number_old(self.val % other)

    def __divmod__(self, other):
        self.repl()
        return (self // other, self % other)

    def __pow__(self, other):
        self.repl()
        return Number_old(self.val ** other)

    def __iadd__(self, other):
        self.repl()
        self.numer += other * self.denom
        self.repl()
        return self.val

    def __isub__(self, other):
        self.repl()
        self.numer -= other * self.denom
        self.repl()
        return self.val

    def __imul__(self, other):
        self.repl()
        self.numer *= other
        self.repl()
        return self.val

    def __itruediv__(self, other):
        self.repl()
        self.denom *= other
        self.repl()
        return self.val

    def __ifloordiv__(self, other):
        self.repl()
        self.numer = self.val // other
        self.denom = 1
        self.repl()
        return self.val

    def __imod__(self, other):
        self.repl()
        self.numer = self.val % other
        self.denom = 1
        self.repl()
        return self.val

    def __ipow__(self, other):
        self.repl()
        self.numer **= other
        self.repl()
        return self.val

    def __abs__(self):
        self.repl()
        return Number_old(abs(self.val))

    def __int__(self):
        self.repl()
        assert not isinstance(self.val, complex)
        return int(self.val)

    def __float__(self):
        self.repl()
        assert not isinstance(self.val, complex)
        return float(self.val)

    def __complex__(self):
        self.repl()
        return complex(self.val)
    


__all__ = [Number_old]
