import math
import copy
import numpy as np

class inputneuron:
    def __init__(self, inputs):
        self.inputs = inputs

    def getOutput(self):
        return self.inputs

    def updateInputs(self, inputs):
        self.inputs = inputs

