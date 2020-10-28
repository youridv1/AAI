class inputneuron:
    """Simple neuron used for the input layer"""
    def __init__(self, inputs):
        self.inputs = inputs

    def getOutput(self):
        """Returns input"""
        return self.inputs

    def receiveWeightedError(self, we):
        """ Receives the weighted errors of the neuron (So fuck all) """
        _ = we

    def updatevalue(self, inputs):
        """ Function to update the inputs of the neuron """
        self.inputs = inputs

    def updateInputs(self):
        """ Updates the inputs (So fuck all)"""
        _ = 1

    def update(self, void):
        """ Updates the weights (So fuck all) """
        _ = void

