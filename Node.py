import math
import random
import numpy as np


class Node:
    def __init__(self, learningRate, type):
        self.learningRate = learningRate
        self.type = type
        self.weights = []
        # Slumpa 400 vikter.
        for i in range(0, 400):
            self.weights.append(random.uniform(0,1))

    def sigmoid(self,x):
        return math.exp(-np.logaddexp(0, -x))

    def teachPerceptron(self, list):
        #meanSqError = 0
        errorSum=0
        for i in range (0, len(list)): # går igenom varje imgObj
            summa = 0
            for j in range(0, len(list[i].picture)): # Går igenom varje pixel/vikt
                summa = summa + (list[i].picture[j]*self.weights[j])
            a = self.sigmoid(summa)
            y = 0
            if list[i].facit == self.type:
                y = 1
            e = y-a
            errorSum= errorSum+ math.fabs(e)
            #meanSqError = meanSqError + (e*e)
            for k in range(0, len(list[i].picture)):
                deltaW = self.learningRate * e * list[i].picture[k]
                self.weights[k] = self.weights[k] + deltaW
        #meanSqError = meanSqError/len(list)
        #return meanSqError
        return errorSum

    def examinePerceptron(self, img):
        #print("vikter: ", self.weights)
        summa = 0
        for j in range(0, len(img.picture)):
            summa = summa + (img.picture[j] * self.weights[j])
        a = self.sigmoid(summa)
        return(a)