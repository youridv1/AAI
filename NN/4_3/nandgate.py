import math
import sigmoidneuron as nr
import inputneuron as ir
import random
import copy
import numpy as np
import time

random.seed(time.time())

inputA = ir.inputneuron(0)
inputB = ir.inputneuron(0)
inputC = ir.inputneuron(0)

inputs = [inputA, inputB, inputC]

bias = ir.inputneuron(1)

weights = []
for i in range(len(inputs)+1):
    weights.append(random.uniform(-1, 1))
print(weights)

norGate = nr.sigmoidneuron(inputs, weights, bias)

trainingset = [
    ([0, 0, 0], 1),
    ([0, 0, 1], 1),
    ([0, 1, 0], 1),
    ([0, 1, 1], 1),
    ([1, 0, 0], 1),
    ([1, 0, 1], 1),
    ([1, 1, 0], 1),
    ([1, 1, 1], 0)
]


oldweights = []
counter = 0
while True:
    delta = [0]*(len(trainingset[0][0])+1)
    oldweights = copy.copy(norGate.weights)
    for z in range(len(trainingset)):

        for k in range(len(trainingset[z][0])):
            inputs[k].updateInputs(trainingset[z][0][k])
        
        norGate.update(trainingset[z][1])

        if counter > 999:
            print(norGate.weights, norGate.getOutput())
    delta += abs(np.subtract(oldweights, norGate.weights))
    if counter > 999:
        print(delta)
        print()
        counter = 0
    else:
        counter += 1
    if max(delta) < 10**-8:
        break

prediction = []
tmp = 0
for i in range(len(inputs)):
    norGate.updateInputs()
    tmp = norGate.getOutput()
    tmp = (tmp >= 0.5) * 1.0
    prediction.append(tmp)
print(prediction)
