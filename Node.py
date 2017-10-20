import math
import random
import numpy as np

class Node:
    def __init__(self, learningRate, type):
        self.learningRate = learningRate
        self.type = type
        self.weights = []

        # Randomizes 400 weights between 0 and 1, these two limits included.
        for i in range(0, 400):
            self.weights.append(random.uniform(0,1))

    def sigmoid(self,x):
        return math.exp(-np.logaddexp(0, -x))

    # Tranverse through the list of images and for each of the images, summarize the weights multiplied with
    # each of the pixel values of that image.
    # The weights are adjusted accordingly and the absolute sum of all the errors are returned.
    def teachPerceptron(self, list):
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
            for k in range(0, len(list[i].picture)):
                deltaW = self.learningRate * e * list[i].picture[k]
                self.weights[k] = self.weights[k] + deltaW

        return errorSum

    # After program has been trained, this function will use the decided weights of the program
    # has concluded and will calculate the sum of the activation function.
    def examinePerceptron(self, img):
        summa = 0
        for j in range(0, len(img.picture)):
            summa = summa + (img.picture[j] * self.weights[j])
        a = self.sigmoid(summa)
        return(a)