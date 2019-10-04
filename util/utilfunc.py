import numpy as np


class UTIL(object):
    def softmax(self, x: np.array) -> np.array:
        """

        :param x:
        :return:
        """
        C = np.max(x)
        return np.exp(x - C) / sum(np.exp(x - C))
