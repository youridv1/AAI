import math
import copy
import numpy as np

class sigmoidneuron:
    def __init__(self, inputs, weights):
        self.weights = weights
        self.output = None
        self.etha = 1
        self.inputs = []
        # print(self.weights)
        for i in range(len(inputs)):
            if type(inputs[i]) == sigmoidneuron:
                self.inputs.append(inputs[i].getOutput())
            else:
                self.inputs.append(inputs[i])
        self.inputAmount = len(self.inputs)

    def getOutput(self):
        total = 0
        if len(self.weights) < 1:
            self.output = self.inputs
            return self.output
        elif len(self.weights) == self.inputAmount:
            for i in range(self.inputAmount):
                total = total + (self.inputs[i] * self.weights[i])
                # print(self.inputs[i], self.weights[i])
            self.output = self.sigmoid(total)
            return self.output
        else:
            print("godverdomme")

    def sigmoid(self, z):
        x = 1/(1+math.exp(-z))
        return x
        # return np.tanh(z)
        

    def derivedSigmoid(self, z):
        x = self.sigmoid(z)
        # return 1-x**2
        return x*(1-x)


    def inK(self, weights):
        total = 0
        for i in range(self.inputAmount):
            total += self.inputs[i] * weights[i]
        return total

    def updateInputs(self, inputs):
        self.inputs = []
        for i in range(len(inputs)):
            if type(inputs[i]) == sigmoidneuron:
                self.inputs.append(inputs[i].getOutput())
            else:
                self.inputs.append(inputs[i])
        self.inputAmount = len(self.inputs)

    def update(self, desired, inputs):

        self.updateInputs(inputs)

        oldweights = copy.copy(self.weights)
        deltaWeights = []
        totalink = self.inK(oldweights)
        for i in range(self.inputAmount):
            deltaWeights.append(self.inputs[i]*self.etha*self.derivedSigmoid(totalink)*(desired-self.getOutput()))
            # print(self.derivedSigmoid(totalink))
        self.weights = np.add(oldweights, deltaWeights)