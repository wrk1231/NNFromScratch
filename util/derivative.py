import numpy as np

class DERIVATIVE(object):

    def numerical_diff(self, func, x):

        h = 1e-4
        return (func(x+h) - func(x-h)) / (2*h)

    