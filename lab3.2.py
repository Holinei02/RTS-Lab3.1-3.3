neural_network.py
from decimal import Decimal


class NeuralNetwork:

    def __init__(self, x1, x2, y1, y2, p=10, sigma=0.1):
        self.x1 = Decimal(str(x1))
        self.x2 = Decimal(str(x2))
        self.y1 = Decimal(str(y1))
        self.y2 = Decimal(str(y2))
        self.p = Decimal(str(p))
        self.sigma = Decimal(str(sigma))
        self.w1 = Decimal(str(0))
        self.w2 = Decimal(str(0))
        self.delta = Decimal(str(0))

    def get_coefs(self):
        return self.w1, self.w2

    def count_coefs1(self):
        # print(self.w1, self.w2)
        ident = False
        res_x = self.x1 * self.w1 + self.x2 * self.w2
        if res_x >= self.p:
            self.delta = self.p - res_x
            self.w1 = self.w1 + self.delta * self.x1 * self.sigma
            self.w2 = self.w2 + self.delta * self.x2 * self.sigma
            ident = True
        res_y = self.y1 * self.w1 + self.y2 * self.w2
        if res_y <= self.p:
            self.delta = self.p - res_y
            self.w1 = self.w1 + self.delta * self.y1 * self.sigma
            self.w2 = self.w2 + self.delta * self.y2 * self.sigma
            ident = True
        if ident:
            return self.count_coefs1()
        return float(self.w1), float(self.w2)

    def calculate_result(self, p1, p2):
        return p1 * self.w1 + p2 * self.w2

    def count_coefs(self):
        count = 0
        z1, z2 = 0, 0
        while z1 >= self.p or z2 <= self.p or count < 1000:
            if z1 >= self.p:
                self.delta = self.p - z1
                self.w1 += self.delta * self.x1 * self.sigma
                self.w2 += self.delta * self.x2 * self.sigma
            elif z2 <= self.p:
                self.delta = self.p - z2
                self.w1 += self.delta * self.y1 * self.sigma
                self.w2 += self.delta * self.y2 * self.sigma
            z1 = self.calculate_result(self.x1, self.x2)
            z2 = self.calculate_result(self.y1, self.y2)
            count += 1
            if count >= 1000:
                print(self.x1, self.x2)
                print(self.y1, self.y2)
                return None
        return self.w1, self.w2
