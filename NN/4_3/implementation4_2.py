import neuron as nr

inputA = nr.neuron(1)
inputB = nr.neuron(1)
inputCi = nr.neuron(1)

OrGate1 = nr.neuron([inputA, inputB], [1, 1], 1)
NandGate1 = nr.neuron([inputA, inputB], [-1, -1], -1)
XORGate1 = nr.neuron([OrGate1, NandGate1], [1, 1], 2)

OrGate2 = nr.neuron([XORGate1, inputCi], [1, 1], 1)
NandGate2 = nr.neuron([XORGate1, inputCi], [-1, -1], -1)
XORGate2 = nr.neuron([OrGate2, NandGate2], [1, 1], 2)

AndGate1 = nr.neuron([inputCi, XORGate1], [1, 1], 2)
AndGate2 = nr.neuron([inputA, inputB], [1, 1], 2)

OrGate3 = nr.neuron([AndGate1, AndGate2], [1, 1], 1)

# print(OrGate3.getOutput(), XORGate2.getOutput())
print(OrGate3.getOutput()*2 + XORGate2.getOutput())