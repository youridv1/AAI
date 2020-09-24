import math
import sigmoidneuron as nr
import random
import copy
import numpy as np
import time

random.seed(time.time())

# inputA = nr.sigmoidneuron(1)
# inputB = nr.sigmoidneuron(1)
# inputC = nr.sigmoidneuron(1)

[1, 1, 1]

desired = 0

weights = []
for i in range(4):
    weights.append(random.uniform(0, 10.0))
print(weights)

norGate = nr.sigmoidneuron([1, 1, 1, 1], weights)

inputs = [
    ([0, 0, 0, 1], 0),
    ([0, 0, 1, 1], 1),
    ([0, 1, 0, 1], 1),
    ([0, 1, 1, 1], 1),
    ([1, 0, 0, 1], 1),
    ([1, 0, 1, 1], 1),
    ([1, 1, 0, 1], 1),
    ([1, 1, 1, 1], 1)
]

oldweights = []
counter = 0
while True:
    delta = [0, 0, 0, 0]
    oldweights = copy.copy(norGate.weights)
    for z in range(len(inputs)):
        # print("Wat in de fuck v2")
        
        norGate.update(inputs[z][1], inputs[z][0])
        
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
    norGate.updateInputs(inputs[i][0])
    tmp = norGate.getOutput()
    tmp = (tmp >= 0.5) * 1.0
    prediction.append(tmp)
print(prediction)
