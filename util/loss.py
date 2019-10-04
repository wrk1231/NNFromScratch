import numpy as np

class LOSS(object):
    def mean_square_error(self, y, target):
        return 0.5 * np.square(target - y)

    def cross_entropy(self,y, target):
        h = 1e-7
        return -np.sum(target * np.log(y +h))
