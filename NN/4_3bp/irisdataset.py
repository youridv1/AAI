import math
import sigmoidneuron as nr
import inputneuron as ir
import random
import copy
import numpy as np
import time
import progressbar

random.seed(0)

def randomWeights(inputs):
    weights = []
    for _ in range(len(inputs)+1):
        weights.append(random.uniform(-1.0, 1.0))
    return weights

datapoints = np.genfromtxt("iris.txt", delimiter=",", usecols=[0,1,2,3])
datalabels = np.genfromtxt("iris.txt", delimiter=",", usecols=[4], converters={4: lambda s: [0,0,1] if int(s) == 1 else ( [0,1,0] if int(s) == 2 else [1,0,0] )} )

trainingset = []
for i in range(len(datapoints)):
    trainingset.append((datapoints[i],datalabels[i]))

indexes = []
validationset = []
for _ in range(24):
    indexes.append(random.randint(0, 149))
for index in indexes:
    validationset.append(trainingset[index])
indexes.sort(reverse=True)
for index in indexes:
    trainingset.pop(index)
    
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
oldweights = []
newweights = []

print("Training")
bar = progressbar.ProgressBar(maxval=20, widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
bar.start()

iterations = 1000
for z in range(iterations):
    for i in range(len(trainingset)):
        for j in range(len(trainingset[i][0])):
            inputlayer[j].updatevalue(trainingset[i][0][j])
        for k in range(len(outputlayer)):
            outputlayer[k].update(trainingset[i][1][k])
    progress = int(z*100/iterations)/5
    bar.update(progress)
bar.finish()
print("Done training")

pred = []
answers = []
tmp = 0
inputs = []
for i in range(len(validationset)):
    pred = []
    for j in range(len(validationset[i][0])):
        inputlayer[j].updatevalue(validationset[i][0][j])
    for neuron in outputlayer:
        tmp = neuron.getOutput()
        if tmp > 0.5:
            tmp = 1
        else:
            tmp = 0
        pred.append(tmp)
    answers.append((pred, validationset[i][1]))


total = 0
for answer in answers:
    print("prediction", answer[0], "correct answer", answer[1])
    if np.array_equal(answer[0], answer[1]):
        total += 1
print("Accuracy:", (total / len(answers)) *100, "%")


        