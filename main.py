import ImageReader
from Node import Node
from random import shuffle
import matplotlib.pyplot as plt

fileName = "training.txt"
facitName = "training-facit.txt"

def main():
    print("#Starting FaceSkynet")

    # Get file names
    #TODO Get filenames from "terminal-parameters"
    # ex. "python faces.py training-file.txt training-facit.txt test-file.txt"

    # import files & Create imgObj-lists
    trainingImgList = ImageReader.parse(fileName, facitName)
    examineImgList = "dsfdsfs" # TODO Import examineImgList

    trainingList = trainingImgList[0:200]
    examineList = trainingImgList[200:300]

    learningRate = 0.003
    nodeList = [] # List to store nodes in
    nodeList.extend([Node(learningRate, 1), Node(learningRate, 2), Node(learningRate, 3), Node(learningRate, 4)])

    examineResult = [] # List to store examine result in, being plotted later..

    for h in range(150): # 150 training sessions
        print("Session: ", h)
        shuffle(trainingList)

        meanSqError = 0
        for p in range(0,4): # Teach each node the training-set of images every session
            meanSqError += nodeList[p].teachPerceptron(trainingList)
        meanSqError = meanSqError/4

        if (h%10) == 0: # Examine nodes every 10 session
            examineResult.append(exmamineNetwork(nodeList, examineList)*100)
            print("MeanSqError: ", meanSqError)

    plt.plot(examineResult)
    plt.xlabel('Session')
    plt.ylabel('Result %')
    plt.title('Perceptron-Network results over time')

    plt.show()

def trainNetworkOnImgList(nodeList, trainList):
    for h in range(150): # 150 training sessions
        shuffle(trainList)
        for p in range(0,4): # Teach each node the training-set of images every session
            nodeList[p].teachPerceptron(trainList)

def exmamineNetwork(nodeList, examList):

    correctTimes = 0
    sessionsRun = 0

    for i in range(0, len(examList)):
        correctAnsver = examList[i].facit

        bestGuess = 0
        bestGuessNode = 0

        # Loops throuh the nodes and let them examine the current img
        for h in range(0,4): # Loops through the node-list
            if(nodeList[h].examinePerceptron(examList[i]) > bestGuess):
                bestGuess = nodeList[h].examinePerceptron(examList[i])
                bestGuessNode = nodeList[h].type
        print("Image{} {}".format(i+1, bestGuessNode))
        shuffle(examList)
        if(bestGuessNode == correctAnsver):
            correctTimes = correctTimes + 1
        sessionsRun = sessionsRun + 1
    print("RESULT Examine session: Correct ", (correctTimes/sessionsRun)*100, " %")
    return correctTimes/sessionsRun

if __name__ == "__main__":
    main()