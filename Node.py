import random
import math
import time

class Node(object):
    weights = [] # 400 vikter
    type = 0 # 1-4
    learningRate = 0.5

    def __init__(self, learningRate, type):
        self.learningRate = learningRate
        self.type = type
        # Slumpa 400 vikter.
        for i in range(399):
            r = random.random()
            self.weights.append(r)

    def teachPerceptron(self, list):
        time.sleep(0.05)
        print(self.weights)
        for i in range (len(list)): # Varje imgObj
            sum = 0
            for j in range(399):
                sum = sum + (list[i].picture[j]*self.weights[j])
                #print(list[i].picture[j], " * ", self.weights[j])
            a = math.tanh(sum)
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
            a = math.tanh(sum)
            #print("Node", self.type, "Says: ", a, "| index: ", i)