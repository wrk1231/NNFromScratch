import numpy as np

class DERIVATIVE(object):

    def numerical_diff(self, func, x):
        """

        :param func: pass in a function to be differentiated
        :param x: a sensible value 
        :return:
        """

        h = 1e-4
        return (func(x+h) - func(x-h)) / (2*h)

