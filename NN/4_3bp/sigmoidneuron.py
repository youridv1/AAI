import math
import copy
import numpy as np

class sigmoidneuron:
    def __init__(self, inputs, weights = [], bias = 1):
        self.weights = weights
        self.output = None
        self.etha = 1
        self.inputs = inputs
        self.bias = bias

        self.inputValues = []
        self.updateInputs()
        
        self.inputAmount = len(self.inputValues)

        self.weightedErrors = []

        self.lastError = 0

    def getOutput(self):
        total = 0
        for i in range(self.inputAmount):
            total += (self.inputValues[i] * self.weights[i])
            # print(self.inputs[i], self.weights[i])
        self.output = self.sigmoid(total)
        return self.output

    def sigmoid(self, z):
        x = 1/(1+math.exp(-z))
        return x

    def derivedSigmoid(self, z):
        x = self.sigmoid(z)
        return x*(1-x)

    def inK(self, weights):
        total = 0
        for i in range(self.inputAmount):
            total += self.inputValues[i] * weights[i]
        return total

    def updateInputs(self):
        self.inputValues = []
        for i in range(len(self.inputs)):
            self.inputValues.append(self.inputs[i].getOutput())
        self.inputValues.append(self.bias.getOutput())

    def receiveWeightedError(self, we):
        self.weightedErrors.append(we)

    def delta(self, totalink, desired):
        if not self.weightedErrors:
            self.lastError = desired-self.getOutput()
        else:
            self.lastError = sum(self.weightedErrors)
        return self.lastError*self.derivedSigmoid(totalink)
        
    def update(self, desired):

        for m in range(len(self.inputs)):
            self.inputs[m].receiveWeightedError(self.weights[m]*self.lastError)

        for neuron in self.inputs:
            neuron.update(None)

        self.updateInputs()

        oldweights = copy.copy(self.weights)
        deltaWeights = []
        totalink = self.inK(oldweights)
        
        for i in range(self.inputAmount):
            deltaWeights.append((self.inputValues[i]*self.etha)*self.delta(totalink, desired))
                                                                                 
        self.weights = np.add(oldweights, deltaWeights)

        self.weightedErrors = []