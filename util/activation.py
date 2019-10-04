import numpy as np


class ACTIVATION(object):

    def sigmoid(self, x: np.array) -> np.array:
        """
        :param x: np.array of np.float
        :return: np.array of np.float
        """
        return 1 / (1 + np.exp(-x))

    def setp_function(self, x: np.array) -> np.array:
        """
        :param x: np.array
        :return: np.array
        """
        y = x > 0
        return y.astype(np.int)

    def relu(self,x:np.array)->np.array:
        """
        Rectified Linear Unit
        :param x: array of np.float
        :return: array of np.float
        """
        return np.maximum(0,x)

