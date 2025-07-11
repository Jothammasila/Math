import collections
from functools import lru_cache
import numpy as np
from gmpy2 import gmpy2


class NormalDistribution():

    def __init__(self) -> str:
        return print("This class implements Normal distribution in statistics and probality.\n")

    def z_score(self, x: int, mu: int, sigma: int) -> float:
        self.z_score = (x - mu) / sigma

        if self.z_score < 0:
            return print(f'z-score is {self.z_score}. {x} is {self.z_score} steps from the mean {mu}.')

        else:
            return print(f'z-score is {self.z_score}. {x} is {self.z_score} steps from the mean {mu}.')

    def impericalRule(self):
        self.notes = """
        If X is a random variable and has a normal distribution with mean µ and standard deviation σ, then the Empirical Rule states that:\n
            • About 68% of the x values lie between –1σ and +1σ of the mean µ (within one standard deviation of the mean).\n
            • About 95% of the x values lie between –2σ and +2σ of the mean µ (within two standard deviations of the mean).\n
            • About 99.7% of the x values lie between –3σ and +3σ of the mean µ (within three standard deviations of the mean).\n
        

            Notice that almost all the x values lie within three standard deviations of the mean.\n
            • The z-scores for +1σ and –1σ are +1 and –1, respectively.\n
            • The z-scores for +2σ and –2σ are +2 and –2, respectively.\n
            • The z-scores for +3σ and –3σ are +3 and –3 respectively.\n
        The empirical rule is also known as the 68-95-99.7 rule."""

        return self.notes

    def z_prob(self):
        pass


class GeometricMean:
    def __init__(self, data):
        self.data = data

    def geometricMean(self):
        for num in self.data:
            pass


class ArithmeticMean:
    def __init__(self, X) -> list:
        self.__x_sum = 0
        self.X = X

    def mean(self) -> float:
        for i in range(len(self.X)):
            self.__x_sum += self.X[i]
        return self.__x_sum / len(self.X)


class Gradient:
    def __init__(self, X, coeff=1, powr=0) -> collections:
        self.X = np.array(X)
        self.coeff = coeff
        self.powr = powr

    def grad(self):

        if self.powr < 0:
            # Check for zero elements in self.X
            # np.isclose(self.X, 0) is used to create a boolean array indicating which elements of 
            # self.X are close to zero. This information is then used to selectively apply the gradient 
            # calculation only to the non-zero elements, preventing division by zero errors.
            zero_elements = np.isclose(self.X, 0)

            # Calculate gradient only for non-zero elements
            return self.coeff * self.powr * (1 / self.X[~zero_elements] ** (np.abs(self.powr - 1)))


        elif self.powr == 0:
            return np.zeros_like(self.X)

        else:
            return self.coeff * self.powr * (self.X ** (self.powr - 1))


class Combinatorics:

    def factorial(self, n):
        self.result = 1
        self.n = n

        if self.n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")

        elif self.n == 0 or self.n == 1:
            return self.result

        else:
            self.result = gmpy2.mpz(1)
            for i in range(1, self.n + 1):
                self.result *= i
            return self.result


def progression_constant(n, const):
    res = int(np.multiply(n, const))
    return res


@lru_cache
def progression_linear(n):
    if isinstance(n, int):
        res = int(np.divide(np.multiply(n, n + 1), 2))
        return res

    else:
        raise TypeError(f'Int Type accepted only but found {type(n)}')


@lru_cache
def progression_squared(n):
    if isinstance(n, int):
        res = int(np.divide((np.multiply(np.multiply(n, n + 1), np.multiply(2, n) + 1)), 6))
        return res

    else:
        raise TypeError(f'Int Type accepted only but found {type(n)}')


@lru_cache
def progression_cubed(n):
    if isinstance(n, int):
        res = int(np.divide(np.multiply(np.square(n), np.square(n + 1)), 4))
        return res

    else:
        raise TypeError(f'Int Type accepted only but found {type(n)}')
