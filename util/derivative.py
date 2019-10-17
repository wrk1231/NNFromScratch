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

    def numerical_gradient(self, func, x):
        """

        :param func: The function to calculate gradient
        :param x: The point to calculate the gradient
        :return:
        """
        h = 1e-4
        grad = np.zeros_like(x)

        for idx in range(x.size):
            temp_val = x[idx]
            x[idx] = temp_val + h
            func_right = func(x)

            x[idx] = temp_val - h
            func_left = func(x)

            grad[idx] = (func_right - func_left)/(2*h)
            x[idx] = temp_val

        return grad
