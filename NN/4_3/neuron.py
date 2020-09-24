import math

class neuron:
    def __init__(self, inputs, weights = None, bias = 0):
        self.inputs = inputs
        self.weights = weights
        self.bias = bias
        self.output = None
        
    def generateOutput(self):
        total = 0
        if self.weights == None:
            self.output = self.inputs
        elif len(self.weights) == len(self.inputs):
            for i in range(len(self.inputs)):
                total += (self.inputs[i].getOutput() * self.weights[i])
            if total >= self.bias:
                self.output = 1
                return
            self.output = 0
        else:
            print("godverdomme")
            
    def getOutput(self):
        if(self.output == None):
            self.generateOutput()
        return self.output

    