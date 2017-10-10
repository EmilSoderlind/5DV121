import ImageReader
import Node
from random import shuffle


fileName = "training.txt"
facitName = "training-facit.txt"

imgList = ImageReader.parse(fileName,facitName)

trainingList = imgList[0:200]
examineList = imgList[200:300]


happyNode = Node.Node(0.01, 1)
angryNode = Node.Node(0.01, 4)
michNode = Node.Node(0.01, 3)
sadNode = Node.Node(0.01, 2)

def exmamineNetwork():

    for i in range(0, 2):
        correctAnsver = examineList[i].facit

        bestGuess = 0
        bestGuessNode = 0

        print("HappyNode: ", happyNode.examinePerceptron(examineList[i]))
        print("angryNode: ", angryNode.examinePerceptron(examineList[i]))
        print("michNode: ", michNode.examinePerceptron(examineList[i]))
        print("sadNode: ", sadNode.examinePerceptron(examineList[i]))

        bestGuess = happyNode.examinePerceptron(examineList[i])
        bestGuessNode = happyNode.type

        if(angryNode.examinePerceptron(examineList[i]) > bestGuess):
            bestGuess = angryNode.examinePerceptron(examineList[i])
            bestGuessNode = angryNode.type

        if(michNode.examinePerceptron(examineList[i]) > bestGuess):
            bestGuess = michNode.examinePerceptron(examineList[i])
            bestGuessNode = michNode.type

        if(sadNode.examinePerceptron(examineList[i]) > bestGuess):
            bestGuess = sadNode.examinePerceptron(examineList[i])
            bestGuessNode = sadNode.type

        print("Nodes think it is ", bestGuessNode, " by ", bestGuess)
        print("Correct type: ", correctAnsver)

for h in range(10):
    sadNode.teachPerceptron(trainingList[0:199])
    michNode.teachPerceptron(trainingList[0:199])
    happyNode.teachPerceptron(trainingList[0:199])
    angryNode.teachPerceptron(trainingList[0:199])
    shuffle(trainingList)
    exmamineNetwork()


