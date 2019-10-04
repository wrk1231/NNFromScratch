import numpy as np

class LOSS(object):
    def mean_square_error(self, x, target):
        return 0.5 * np.square(target - x)

    def cross_entropy(self):
        pass
