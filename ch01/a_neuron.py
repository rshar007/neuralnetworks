#!/usr/bin/python

import numpy as np

'''Implementation of a simple artificial neuron in Python.'''

class Neuron:
    def __init__(self, weights, bias, function):
        self.weights = weights
        self.bias = biad
        self.function = function

    def forward(self, inputs):
        logit = np.dot(inputs, self.weights) + self.bias
        output = self.function(logit)
        return output


