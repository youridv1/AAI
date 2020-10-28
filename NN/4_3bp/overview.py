class sigmoidneuron:
    """ Neuron class using the sigmoid activation function. """
    def __init__(self, inputs, weights = [], bias = 1):
        """ Constructor for sigmoid neuron """

    def getOutput(self):
        """ Returns the output of the activation function of the neuron """

    def sigmoid(self, z):
        """ Sigmoid function """

    def derivedSigmoid(self, z):
        """ Derivitive of the sigmoid function """

    def inK(self, weights):
        """ Total of the input values """

    def updateInputs(self):
        """ Updates the inputvalues """
    
    def receiveWeightedError(self, we):
        """ appends the argument we to the weighted errors of the neuron """

    def delta(self, totalink, desired):
        """ Returns the errorfuit's the last neuron in the networknction of the neuron """

    def update(self, desired):
        """Updates the weights of the neuron and uses backpropagation to update all neurons in previous layers"""

class inputneuron:
    """Simple neuron used for the input layer"""
    def __init__(self, inputs):

    def getOutput(self):
        """Returns input"""

    def receiveWeightedError(self, we):
        """ Receives the weighted errors of the neuron (So fuck all) """

    def updatevalue(self, inputs):
        """ Function to update the inputs of the neuron """

    def updateInputs(self):
        """ Updates the inputs (So fuck all)"""

    def update(self, void):
        """ Updates the weights (So fuck all) """


#Main script for training the neural network for Iris classification
import math
import sigmoidneuron as nr
import inputneuron as ir
import random
import copy
import numpy as np
import time
import progressbar

#Generates a given amount of random weights
def randomWeights(inputs):
    weights = []
    for _ in range(len(inputs)+1):
        weights.append(random.uniform(-1.0, 1.0))
    return weights


#Setting the training and validation data
datapoints = np.genfromtxt("iris.txt", delimiter=",", usecols=[0,1,2,3])
datalabels = np.genfromtxt("iris.txt", delimiter=",", usecols=[4], converters={4: lambda s: [0,0,1] if int(s) == 1 else ( [0,1,0] if int(s) == 2 else [1,0,0] )} )

trainingset = []
for i in range(len(datapoints)):
    trainingset.append((datapoints[i],datalabels[i]))

indexes = []
validationset = []
for _ in range(24):
    indexes.append(random.randint(0, 149))  #Choose 24 random datapoints to add to the validation set and remove from trainingset
for index in indexes:
    validationset.append(trainingset[index])
indexes.sort(reverse=True)  # Sort the list descending so we don't have any problems with the list items shifting positions
for index in indexes:
    trainingset.pop(index)


#Creating some layers
bias = ir.inputneuron(1)

inputlayer = []
for _ in range(4):
    inputlayer.append(ir.inputneuron(0))

hiddenlayer = []
for _ in range(5):
    hiddenlayer.append(nr.sigmoidneuron(inputlayer, randomWeights(inputlayer), bias))

outputlayer = []
for _ in range(3):
    outputlayer.append(nr.sigmoidneuron(hiddenlayer, randomWeights(hiddenlayer), bias))

# trainingloop
print("Training")
bar = progressbar.ProgressBar(maxval=20, widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()]) #Yes. A progress bar. Deal with it
bar.start()

iterations = 1000
for z in range(iterations): #Train for given amount of iterations
    for i in range(len(trainingset)): #Iterate over the trainingset and set the input neurons
        for j in range(len(trainingset[i][0])):
            inputlayer[j].updatevalue(trainingset[i][0][j])
        for k in range(len(outputlayer)): #Update weights
            outputlayer[k].update(trainingset[i][1][k])
    progress = int(z*100/iterations)/5 #Progress bar stuff
    bar.update(progress)
bar.finish()
print("Done training")

#Validationloop
pred = []
answers = []
tmp = 0
inputs = []
for i in range(len(validationset)):
    pred = []
    for j in range(len(validationset[i][0])): #Update input of network
        inputlayer[j].updatevalue(validationset[i][0][j])
    for neuron in outputlayer:
        tmp = neuron.getOutput() #Get a prediction
        if tmp > 0.5:
            tmp = 1
        else:
            tmp = 0
        pred.append(tmp)
    answers.append((pred, validationset[i][1])) #Append prediction and correct answer to list

#Checking predictions with the correct answer
total = 0
for answer in answers:
    print("prediction", answer[0], "correct answer", answer[1])
    if np.array_equal(answer[0], answer[1]):
        total += 1
print("Accuracy:", total / len(answers)) #Calculate percentage of answers correct