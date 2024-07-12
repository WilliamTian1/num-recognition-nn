import numpy
import scipy.special
class neuralNetwork:
    def __init__(self, inputNodes,hiddenNodes, outputNodes, learningrate):
        self.inodes = inputNodes
        self.hnodes =  hiddenNodes
        self.onodes = outputNodes
        self.lr = learningrate
        self.wih = numpy.random.normal(0.0, pow(self.hnodes, -0.5),(self.hnodes, self.inodes))
        self.who = numpy.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hodes))
        pass
    def train(self, inputs_list, targets_list): 
        #convert inputs_list and target_list into 2D array for matrix multiplication
        inputs = numpy.array(inputs_list, ndmin=2).T
        targets = numpy.array(targets_list, ndmin=2).T
        hiddenInputs = numpy.dot(self.wih, inputs)
        self.activation = lambda x: scipy.special.expit(x)
        hiddenOutputs = self.activation(hiddenInputs)
        outputInputs = numpy.dot(self.who, hiddenOutputs)
        outputOutputs = self.activation(outputInputs)
        outputErrors = targets - outputOutputs
        hiddenErrors =numpy.dot(self.who, outputErrors)
        # update the weights for the links between the hidden and output layers
        self.who += self.lr * numpy.dot((outputErrors * outputOutputs * (1.0 -
        outputOutputs)), numpy.transpose(hiddenOutputs))
        self.wih += self.lr * numpy.dot((hiddenErrors*hiddenOutputs*(1.0 - hiddenOutputs)),
        numpy.transpose(hiddenInputs))
        pass
    def query(self, inputs_list):
        #convert inputs_list into 2D array for matrix multiplication
        inputs = numpy.array(inputs_list, ndmin=2).T
        hiddenInputs = numpy.dot(self.wih, inputs)
        self.activation = lambda x: scipy.special.expit(x)
        hiddenOutputs = self.activation(hiddenInputs)
        outputInputs = numpy.dot(self.who, hiddenOutputs)
        outputOutputs = self.activation(outputInputs)
        return outputOutputs
        pass