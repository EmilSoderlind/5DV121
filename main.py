import ImageReader
from Node import Node
from random import shuffle
import sys

def main():
    # Checks the number of arguments and if the number is wrong, a
    # message telling this will be sent to stdout and the program ends,
    if(len(sys.argv) == 4):
        trainingListFileName = sys.argv[1]
        trainingFacitFileName = sys.argv[2]
        examineFileName = sys.argv[3]
    else:
        print("Wrong number of arguments")
        exit(-1)

    # The Image objects of the user included traininglist will be built and added to the list.
    # Same with the file the program will use to test its training on in the end.
    defaultTestImgList = ImageReader.parse(trainingListFileName,trainingFacitFileName)
    examineImgList = ImageReader.parseTest(examineFileName)


    learningRate = 0.1

    # A list with the four node types are built, the number 1-4 represents a mood/ smile type.
    nodeList = []
    nodeList.extend([Node(learningRate, 1), Node(learningRate, 2), Node(learningRate, 3), Node(learningRate, 4)])

    # The program is trained
    trainNetworkOnImgList(nodeList,defaultTestImgList)

    # The program puts its training to the test with the user included test file.
    exmamineNetwork(nodeList,examineImgList,True)

# Train the perceptron as long as the absolut error from the run is less than 10.
# Every loop teaches each of the node types the training-set of images every session.
def trainNetworkOnImgList(nodeList, trainList):
    errorSum=1000
    while(errorSum > 10):
        errorSum=0
        shuffle(trainList)
        for p in range(0,4):
            errorSum= errorSum + nodeList[p].teachPerceptron(trainList)

# Perceptron examine each of the images in the testlist with unseen images, prints the result to stdout
def exmamineNetwork(nodeList, examList, showResult):
    for i in range(0, len(examList)):

        bestGuess = 0
        bestGuessNode = 0

        # Loops through the list of nodes and let them examine the current image the test file.
        # The node with the highest result from the nodes activation function will claim the
        # picture to be the same type/mood as itself.
        for h in range(0,len(nodeList)):
            if(nodeList[h].examinePerceptron(examList[i]) > bestGuess):
                bestGuess = nodeList[h].examinePerceptron(examList[i])
                bestGuessNode = nodeList[h].type

        if(showResult):
            print("Image{} {}".format(i+201, bestGuessNode))

if __name__ == "__main__":
    main()