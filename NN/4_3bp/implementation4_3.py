import math
import sigmoidneuron as nr
import inputneuron as ir
import random
import copy
import numpy as np
import time

random.seed(0)

def randomWeights(inputs):
    weights = []
    for _ in range(len(inputs)+1):
        weights.append(random.uniform(-1.0, 1.0))
    return weights

inputA = ir.inputneuron(0)
inputB = ir.inputneuron(0)
bias1 = ir.inputneuron(0.5)
bias2 = ir.inputneuron(3)

inputs = [inputA, inputB]

NANDweights = randomWeights(inputs)
NAND = nr.sigmoidneuron(inputs, NANDweights, bias1)

ORweights = randomWeights(inputs)
OR = nr.sigmoidneuron(inputs, ORweights, bias1)

ANDinputs = [NAND, OR]
ANDweights = randomWeights(ANDinputs)
AND = nr.sigmoidneuron(ANDinputs, ANDweights, bias2)

trainingset = [
    ([1, 0], 1),    
    ([0, 0], 0),
    ([0, 1], 1),
    ([1, 1], 0)
]

oldweights = []
counter = 0
outputs = [0]*len(trainingset)
for _ in range(100000):
    # random.shuffle(trainingset)
    delta = [0]*(len(ANDinputs)+1)
    oldweights = copy.copy(AND.weights)
    for z in range(len(trainingset)):

        for k in range(len(trainingset[z][0])):
            inputs[k].updateInputs(trainingset[z][0][k])
        
        AND.update(trainingset[z][1])
        outputs[z] = [AND.getOutput(), trainingset[z][1]]
        if counter > 999:
            print(AND.weights, AND.getOutput(), trainingset[z])
    delta += abs(np.subtract(oldweights, AND.weights))
    if counter > 999:
        print(delta)
        print()
        counter = 0
    else:
        counter += 1
    if max(delta) < 10**-9:
        break

# prediction = []
# tmp = 0
# for i in range(len(trainingset)):
#     AND.updateInputs()
#     tmp = AND.getOutput()
#     print(tmp)
#     tmp = (tmp >= 0.5) * 1.0
#     prediction.append(tmp)
for i in range(len(outputs)):
    outputs[i][0] = (outputs[i][0] >= 0.5) * 1.0
print(outputs)
