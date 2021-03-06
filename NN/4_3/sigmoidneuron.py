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
        # return np.tanh(z)
        

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
        

    def update(self, desired):

        self.updateInputs()

        oldweights = copy.copy(self.weights)
        deltaWeights = []
        totalink = self.inK(oldweights)
        for i in range(self.inputAmount):
            deltaWeights.append((self.inputValues[i]*self.etha)*self.derivedSigmoid(totalink)*(desired-self.getOutput()))
        self.weights = np.add(oldweights, deltaWeights)