Genetic_algorithm.py
from random import randint, random, choice


class GeneticAlgorithm:

    def __init__(self, ca=1, cb=3, cc=1, f=15, number=4, minr=1, maxr=10, limit=1000, maxn=7):
        self.coef = [ca, cb, cc, f]
        self.number = number
        self.minr = minr
        self.maxr = maxr
        self.limit = limit
        self.maxn = maxn

    def count_survival(self, gen):
        res = -self.coef[-1]
        for i in range(len(self.coef) - 1):
            res += self.coef[i] * gen[i]
        return res

    def get_gens(self):
        res = [randint(self.minr, self.maxr) for _ in range(len(self.coef) - 1)]
        if self.count_survival(res) == 0:
            res = self.get_gens()
        return res

    @staticmethod
    def get_random_gens(gens, genslc):
        rand = random()
        for i in range(len(gens)):
            if rand <= genslc[i]:
                return gens[i]

    @staticmethod
    def get_children(father, mother):
        res = []
        for i in range(len(father)):
            if randint(0, 1) == 0:
                res.append(father[i])
            else:
                res.append(mother[i])
        return res

    def mutate(self, gen):
        if randint(0, self.maxn) == 0:
            gen[randint(0, len(gen) - 1)] += choice([-1, 1])
        return gen

    def get_new_generation(self, gens):
        genslc = [1 / abs(self.count_survival(i)) for i in gens]
        gensum = sum(genslc)
        genslc[0] /= gensum
        for i in range(1, len(genslc)):
            genslc[i] /= gensum
            genslc[i] += genslc[i - 1]
        return [self.mutate(self.get_children(self.get_random_gens(gens, genslc), self.get_random_gens(gens, genslc)))
                for _ in gens]

    def count_gen_with_coefs(self, gen):
        return sum([self.coef[i] * gen[i] for i in range(len(gen))])

    def solve(self):
        gens = [self.get_gens() for _ in range(self.number)]
        for i in range(self.limit):
            yield gens
            for g in gens:
                if self.count_survival(g) == 0:
                    yield g
                    return
            gens = self.get_new_generation(gens)
        yield ['{} = {}'.format(gen, self.count_gen_with_coefs(gen)) for gen in gens]
        return
