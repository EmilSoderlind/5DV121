import random
import math
import time

class Node(object):
    weights = [] # 400 vikter
    type = 0 # 1-4
    learningRate = 0.1

    def __init__(self, learningRate, type):
        self.learningRate = learningRate
        self.type = type
        # Slumpa 400 vikter.
        for i in range(0, 400):
            r = random.random()
            self.weights.append(r)

    def teachPerceptron(self, list):
        for i in range (0, len(list)): # går igenom varje imgObj
            sum = 0
            for j in range(0, len(list[i].picture)): # Går igenom varje pixel/vikt
                sum = sum + (list[i].picture[j]*self.weights[j])
            a = math.tanh(sum)
            y = 0
            if(list[i].facit == self.type):
                y = 1
            e = y-a
            for k in range(0, len(list[i].picture)):
                deltaW = self.learningRate * e * list[i].picture[k]
                self.weights[k] = self.weights[k] + deltaW

    def examinePerceptron(self, img):
        sum = 0
        for j in range(0, len(img.picture)):
            sum = sum + (img.picture[j] * self.weights[j])
        a = math.tanh(sum)
        return(a)