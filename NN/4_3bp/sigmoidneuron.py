import math
import copy
import numpy as np
import time

class sigmoidneuron:
    """ Neuron class using the sigmoid activation function. """
    def __init__(self, inputs, weights = [], bias = 1):
        """ Constructor for sigmoid neuron """
        self.weights = weights
        self.output = None
        self.etha = 0.1
        self.inputs = inputs
        self.bias = bias

        self.inputValues = []
        self.updateInputs()
        
        self.inputAmount = len(self.inputValues)

        self.weightedErrors = []

        self.lastError = 0

    def getOutput(self):
        """ Returns the output of the activation function of the neuron """
        total = 0
        for i in self.inputs: #Update all input values
            i.updateInputs()
        self.updateInputs()
        for i in range(self.inputAmount):
            total += (self.inputValues[i] * self.weights[i])
        self.output = self.sigmoid(total)
        return self.output

    def sigmoid(self, z):
        """ Sigmoid function """
        x = 1/(1+math.exp(-z))
        return x

    def derivedSigmoid(self, z):
        """ Derivitive of the sigmoid function """
        x = self.sigmoid(z)
        return x*(1-x)

    def inK(self, weights):
        """ Total of the input values """
        total = 0
        for i in range(self.inputAmount):
            total += self.inputValues[i] * weights[i]
        return total

    def updateInputs(self):
        """ Updates the inputvalues """
        self.inputValues = []
        for i in range(len(self.inputs)):
            self.inputValues.append(self.inputs[i].getOutput())
        self.inputValues.append(self.bias.getOutput())

    def receiveWeightedError(self, we):
        """ appends the argument we to the weighted errors of the neuron """
        self.weightedErrors.append(we)

    def delta(self, totalink, desired):
        """ Returns the errorfunction of the neuron """
        if not self.weightedErrors: #If outputneuron
            self.lastError = desired-self.getOutput()
        else:
            self.lastError = sum(self.weightedErrors) #If not outputneuron
        return self.lastError*self.derivedSigmoid(totalink)
        
    def update(self, desired):
        """Updates the weights of the neuron and uses backpropagation to update all neurons in previous layers"""
        for m in range(len(self.inputs)):
            self.inputs[m].receiveWeightedError(self.weights[m]*self.lastError) #Give inputs their weighted error

        for neuron in self.inputs:
            neuron.update(None) # Calls update on all previous neurons

        self.updateInputs() # Gets the output of all input neurons

        oldweights = copy.copy(self.weights)
        deltaWeights = []
        totalink = self.inK(oldweights)
        
        for i in range(self.inputAmount):
            deltaWeights.append((self.inputValues[i]*self.etha)*self.delta(totalink, desired)) #Calculates delta to be applied to weights
                                                                                 
        self.weights = np.add(oldweights, deltaWeights)

        self.weightedErrors = []