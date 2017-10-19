import ImageReader
from Node import Node
from random import shuffle
import matplotlib.pyplot as plt
import sys


def main():
    print("#Starting FaceSkynet")

    trainingListFileName = "training-A.txt"
    trainingFacitFileName = "facit-A.txt"
    examineFileName = "test-B.txt"

    if(len(sys.argv) == 4):
        trainingListFileName = sys.argv[1]
        trainingFacitFileName = sys.argv[2]
        examineFileName = sys.argv[3]


    defaultTestImgList = ImageReader.parse(trainingListFileName,trainingFacitFileName)
    examineImgList = ImageReader.parseTest(examineFileName)

    learningRate = 0.003
    nodeList = [] # List to store nodes in
    nodeList.extend([Node(learningRate, 1), Node(learningRate, 2), Node(learningRate, 3), Node(learningRate, 4)])

    trainingPart = 0.8
    trainingImgList = defaultTestImgList[0:int(len(defaultTestImgList)*trainingPart)]
    trainingExamImgList = defaultTestImgList[int(len(defaultTestImgList)*trainingPart):len(defaultTestImgList)]

    print("trainingImgList: LEN ", len(trainingImgList))
    #print("trainingExamImgList: ", trainingExamImgList)

    # TODO Träna på training tills trainingExam > X %
    trainNetworkOnImgList(nodeList,trainingImgList,trainingExamImgList)


    # TODO Kör ExamineList och printa ut resultat

def oldMain():
    print("#Starting FaceSkynet")

    #TODO Get filenames from "terminal-parameters"
    # ex. "python faces.py training-file.txt training-facit.txt test-file.txt"

    # import files & Create imgObj-lists
    trainingImgList = ImageReader.parse(fileName, facitName)
    examineImgList = "dsfdsfs" # TODO Import examineImgList

    trainingList = trainingImgList[0:200] # TODO Remove when we use ".txt" files
    examineList = trainingImgList[200:300] # TODO Remove when we use ".txt" files

    learningRate = 0.003
    nodeList = [] # List to store nodes in
    nodeList.extend([Node(learningRate, 1), Node(learningRate, 2), Node(learningRate, 3), Node(learningRate, 4)])

    # TODO Train on training-file.txt + training-facit.txt

    # TODO Examine on test-file.txt

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

# Train the perceptron with a list of images & facit in 150 sessions
def trainNetworkOnImgList(nodeList, trainList, trainingExamImgList):
    for h in range(150): # 150 training sessions
        shuffle(trainList)
        for p in range(0,4): # Teach each node the training-set of images every session
            nodeList[p].teachPerceptron(trainList)
        print(exmamineNetwork(nodeList, trainingExamImgList))

# Examine the perceptron on a examlist of unseen images, prints to console the result
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