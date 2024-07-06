import numpy
import scipy.special
class NeuralNetwork:
    def __init__(self, inputNodes,hiddenNodes, outputNodes, learningrate):
        self.inodes = inputNodes
        self.hnodes =  hiddenNodes
        self.onodes = outputNodes
        self.lr = learningRate
        self.wih = numpy.random.normal(0.0, pow(self.hnodes, -0.5),(self.hnodes, self.inodes))
        self.who = numpy.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hodes))
        pass
    def train(self, inputs_list, targets_list): 
        #convert inputs_list into 2D array for matrix multiplication
        hiddenInputs = numpy.dot(self.wih, inputs)
        self.activation = lambda(x): scipy.special.expit(x)
        hiddenOuputs = self.activation(hiddenInputs)
        outputInputs = numpy.dot(self.who, hiddenOutputs)
        outputOutputs = self.activation(outputInputs)
        outputErrors = targets - outputOutputs

        pass
    def query(self, inputs_list):
        #convert inputs_list into 2D array for matrix multiplication
        hiddenInputs = numpy.dot(self.wih, inputs)
        self.activation = lambda(x): scipy.special.expit(x)
        hiddenOuputs = self.activation(hiddenInputs)
        outputInputs = numpy.dot(self.who, hiddenOutputs)
        outputOutputs = self.activation(outputInputs)
        return outputOutputs
        pass