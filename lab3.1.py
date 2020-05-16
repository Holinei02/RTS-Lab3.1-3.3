class EuclideanAlgorithm:

    def __init__(self, a, b=None):
        self.a = a
        self.b = b
        self.factorized = [1]

    def gcd_rest(self):
        while self.b != 0:
            temp = self.b
            self.b = self.a % self.b
            self.a = temp
        return self.a

    def gcd_difference(self):
        while self.a != self.b:
            if self.a > self.b:
                self.a -= self.b
            else:
                self.b -= self.a
        return self.a

    def gcd_recursion(self):
        if self.b == 0:
            return self.a
        else:
            return EuclideanAlgorithm(self.b, self.a % self.b).gcd_recursion()

    def full_factorization(self, i=2):
        while i <= self.a:
            e = EuclideanAlgorithm(self.a, i).gcd_difference()
            if e == 1:
                i += 1
            else:
                self.factorized.append(i)
                self.a = self.a // i
                return self.full_factorization(i)

    def get_result(self):
        return self.factorized

fermat_algorithm.py
from math import ceil, sqrt

class FermatAlgorithm:

    def __init__(self, n):
        self.n = n
        self.x = ceil(sqrt(self.n))
        self.factorized = []

    def factorization(self):
        y = self.x ** 2 - self.n
        if sqrt(y).is_integer():
            return self.x + sqrt(y), self.x - sqrt(y)
        self.x += 1
        return self.factorization()

    def full_factorization(self):
        f = FermatAlgorithm(self.n).factorization()
        self.factorized.append(f)
        if 1 not in f:
            for i in f:
                self.n = i
                self.full_factorization()

    def get_result(self):
        result = [1]
        for i in self.factorized:
            if 1 in i:
                result.append(int(i[0]))
        return result
