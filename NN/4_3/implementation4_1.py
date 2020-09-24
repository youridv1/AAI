import neuron as nr

inputA = nr.neuron(0)
inputB = nr.neuron(0)
inputC = nr.neuron(0)

norGate = nr.neuron([inputA, inputB, inputC], [-1,-1,-1], 0)
print(norGate.getOutput())

