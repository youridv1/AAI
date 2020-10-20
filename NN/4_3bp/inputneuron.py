import math
import copy
import numpy as np

class inputneuron:
    def __init__(self, inputs):
        self.inputs = inputs

    def getOutput(self):
        return self.inputs

    def receiveWeightedError(self, we):
        _ = we

    def updateInputs(self, inputs):
        self.inputs = inputs

    def update(self, void):
        _ = void

