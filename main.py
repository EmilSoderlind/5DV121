import ImageReader
from Node import Node
from random import shuffle
import matplotlib.pyplot as plt
import sys
def oldMain():
    print("#Starting FaceSkynet")

    #    TODO Get filenames from "terminal-parameters"
    # ex. "python faces.py training-file.txt training-facit.txt test-file.txt"

    #fileName = "training-A.txt"
    #facitName = "facit-A.txt"
    #examineFileName = "test-B.txt"

    if(len(sys.argv) == 4):
        fileName = sys.argv[1]
        facitName = sys.argv[2]
        examineFileName = sys.argv[3]

    # import files & Create imgObj-lists
    trainingImgList = ImageReader.parse(fileName, facitName)
    examineImgList = "dsfdsfs" # TODO Import examineImgList

    trainingList = trainingImgList[0:100] # TODO Remove when we use ".txt" files
    examineList = trainingImgList[100:200] # TODO Remove when we use ".txt" files

    learningRate = 0.1
    nodeList = [] # List to store nodes in
    nodeList.extend([Node(learningRate, 1), Node(learningRate, 2), Node(learningRate, 3), Node(learningRate, 4)])

    # TODO Train on training-file.txt + training-facit.txt

    # TODO Examine on test-file.txt

    examineResult = [] # List to store examine result in, being plotted later..
    errorSum = 100

    while(errorSum > 0.5): # 150 training sessions
        shuffle(trainingList)

        errorSum = 0
        for p in range(0,4): # Teach each node the training-set of images every session
            errorSum = errorSum + nodeList[p].teachPerceptron(trainingList)

        #if (h%10) == 0: # Examine nodes every 10 session
        examineResult.append(exmamineNetwork(nodeList, examineList,True)*100)
        print("ErrorSum: ", errorSum)


    examineImgList = ImageReader.parseTest(examineFileName)
    exmamineNetwork(nodeList,examineImgList,True)


    plt.plot(examineResult)
    plt.xlabel('Session')
    plt.ylabel('Result %')
    plt.title('Perceptron-Network results over time')

    plt.show()


def main():

    trainingListFileName = "training-A.txt"
    trainingFacitFileName = "facit-A.txt"
    examineFileName = "test-B.txt"

    if(len(sys.argv) == 4):
        trainingListFileName = sys.argv[1]
        trainingFacitFileName = sys.argv[2]
        examineFileName = sys.argv[3]


    defaultTestImgList = ImageReader.parse(trainingListFileName,trainingFacitFileName)
    examineImgList = ImageReader.parseTest(examineFileName)

    learningRate = 0.1
    nodeList = [] # List to store nodes in
    nodeList.extend([Node(learningRate, 1), Node(learningRate, 2), Node(learningRate, 3), Node(learningRate, 4)])

    trainingPart = 0.75
    trainingImgList = defaultTestImgList[0:int(len(defaultTestImgList)*trainingPart)]
    trainingExamImgList = defaultTestImgList[int(len(defaultTestImgList)*trainingPart):len(defaultTestImgList)]

    trainNetworkOnImgList(nodeList,trainingImgList,trainingExamImgList)

    exmamineNetwork(nodeList,examineImgList,True)

# Train the perceptron as long as the
def trainNetworkOnImgList(nodeList, trainList, trainingExamImgList):
    errorSum=1000
    while(errorSum > 10):
        errorSum=0
        shuffle(trainList)
        for p in range(0,4): # Teach each node the training-set of images every session
            errorSum= errorSum + nodeList[p].teachPerceptron(trainList)
            #print (errorSum)

# Examine the perceptron on a examlist of unseen images, prints to console the result
def exmamineNetwork(nodeList, examList, showResult):

    correctTimes = 0
    sessionsRun = 1

    for i in range(0, len(examList)):
        correctAnsver = examList[i].facit

        bestGuess = 0
        bestGuessNode = 0

        # Loops throuh the nodes and let them examine the current img
        for h in range(0,4): # Loops through the node-list
            if(nodeList[h].examinePerceptron(examList[i]) > bestGuess):
                bestGuess = nodeList[h].examinePerceptron(examList[i])
                bestGuessNode = nodeList[h].type

        if(showResult):
            print("Image{} {}".format(i+201, bestGuessNode))
        if(bestGuessNode == correctAnsver):
            correctTimes = correctTimes + 1
        sessionsRun = sessionsRun + 1

    #print("RESULT Examine session: Correct ", (correctTimes/sessionsRun)*100, " %")
    return correctTimes/sessionsRun

if __name__ == "__main__":
    main()