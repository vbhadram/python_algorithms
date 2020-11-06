import numpy as np
import matplotlib.pyplot as plt


def poly(n):
    def polyXN(x):
        return x ** n

    return polyXN


fns = [np.log, poly(1), poly(2), poly(3), np.exp]
clrs = ['c', 'b', 'm', 'y', 'r']


def compareAsymptotic(n):
    x = np.arange(1, n, 1)
    plt.title('O(n) for n =' + str(n))
    for f, c in zip(fns, clrs):
        plt.plot(x, f(x), c)
    plt.show()


compareAsymptotic(3)
compareAsymptotic(5)
compareAsymptotic(10)
compareAsymptotic(20)
