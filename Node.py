import random
import math

class Node(object):
    weights = [] # 400 vikter
    type = 0 # 1-4
    learningRate = 0.5

    def __init__(self, learningRate, type):
        self.learningRate = learningRate
        self.type = type
        # Slumpa 400 vikter.
        for i in range(399):
            self.weights.append(random.random())

    def teachPerceptron(self, list):
        for i in range (len(list)): # Varje imgObj
            sum = 0
            for j in range(399):
                sum = sum + (list[i].picture[j]*self.weights[j])
            a = self.sigmoid(sum)
            y = 0
            if(list[i].facit == type):
                y = 1
            e = y-a
            for k in range(399):
                deltaW = self.learningRate*e*list[i].picture[k]
                self.weights[k] = self.weights[k] + deltaW

    def examinePerceptron(self, list):
        for i in range (len(list)): # Varje imgObj
            sum = 0
            for j in range(399):
                sum = sum + (list[i].picture[j]*self.weights[j])
            a = self.sigmoid(sum)
            print("Node", self.type, "Says: ", a, "| index: ", i)

    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))