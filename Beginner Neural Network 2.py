import numpy as np
from collections import Counter
class Perceptron:

	def __init__(self, input_length, weights = None):
		if weights == None:
			self.weights = np.random.random((input_length)) * 2 - 1
		self.learning_rate = 0.1