import ImageReader
from Node import Node
from random import shuffle
import matplotlib.pyplot as plt

fileName = "training.txt"
facitName = "training-facit.txt"

imgList = ImageReader.parse(fileName,facitName)

trainingList = imgList[0:200]
examineList = imgList[200:300]

happyNode = Node(0.003, 1)
angryNode = Node(0.003, 4)
michNode = Node(0.003, 3)
sadNode = Node(0.003, 2)

def exmamineNetwork(examList):

    correctTimes = 0
    sessionsRun = 0

    for i in range(0, len(examList)):
        correctAnsver = examList[i].facit

        bestGuess = 0
        bestGuessNode = 0

        #print("HappyNode: ", happyNode.examinePerceptron(examineList[i]))
        #print("angryNode: ", angryNode.examinePerceptron(examineList[i]))
        #print("michNode: ", michNode.examinePerceptron(examineList[i]))
        #print("sadNode: ", sadNode.examinePerceptron(examineList[i]))

        bestGuess = happyNode.examinePerceptron(examList[i])
        bestGuessNode = happyNode.type

        if(angryNode.examinePerceptron(examList[i]) > bestGuess):
            bestGuess = angryNode.examinePerceptron(examList[i])
            bestGuessNode = angryNode.type

        if(michNode.examinePerceptron(examList[i]) > bestGuess):
            bestGuess = michNode.examinePerceptron(examList[i])
            bestGuessNode = michNode.type

        if(sadNode.examinePerceptron(examList[i]) > bestGuess):
            bestGuess = sadNode.examinePerceptron(examList[i])
            bestGuessNode = sadNode.type

        #print("Nodes think it is ", bestGuessNode, " by ", bestGuess)
        #print("Correct type: ", correctAnsver)
        shuffle(examList)
        if(bestGuessNode == correctAnsver):
            correctTimes = correctTimes + 1
        sessionsRun = sessionsRun + 1

    print("RESULT Examine session: Correct ", (correctTimes/sessionsRun)*100, " %")
    return correctTimes/sessionsRun

examineResult = []

#index = 0
#while True:
#    print("Session: ", index)
#    shuffle(trainingList)
#    meanSqError = sadNode.teachPerceptron(trainingList[0:200])
#    meanSqError = meanSqError + michNode.teachPerceptron(trainingList[0:200])
#    meanSqError = meanSqError + happyNode.teachPerceptron(trainingList[0:200])
#    meanSqError = meanSqError + angryNode.teachPerceptron(trainingList[0:200])
#    meanSqError = meanSqError/4
#
#    examineResult.append(exmamineNetwork()*100)
#    print("Training-Set MeanSqError: ", meanSqError)
#    index += 1
#    if meanSqError < 0.00025:
#        break

for h in range(150):
    print("Session: ", h)
    shuffle(trainingList)
    meanSqError = sadNode.teachPerceptron(trainingList[0:200])
    meanSqError = meanSqError + michNode.teachPerceptron(trainingList[0:200])
    meanSqError = meanSqError + happyNode.teachPerceptron(trainingList[0:200])
    meanSqError = meanSqError + angryNode.teachPerceptron(trainingList[0:200])
    meanSqError = meanSqError/4

    if (h%10) == 0:
        examineResult.append(exmamineNetwork(examineList)*100)
        print("MeanSqError: ", meanSqError)

plt.plot(examineResult)
plt.xlabel('Session')
plt.ylabel('Result %')
plt.title('Perceptron-Network results over time')

plt.show()
