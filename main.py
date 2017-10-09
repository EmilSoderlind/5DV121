import ImageReader
import Node

fileName = "training.txt"
facitName = "training-facit.txt"

imgList = ImageReader.parse(fileName,facitName)

happyNode = Node.Node(0.5, 1)
#angryNode = Node.Node(0.5, 4)
#michNode = Node.Node(0.5, 3)
#sadNode = Node.Node(0.5, 2)

happyNode.teachPerceptron(imgList[0:200])
#angryNode.teachPerceptron(imgList[0:199])
#michNode.teachPerceptron(imgList[0:199])
#sadNode.teachPerceptron(imgList[0:199])

#for i in range(200,300):
    #print(i,"|", happyNode.type,"--> ", happyNode.examinePerceptron(imgList[i]))
    #print(i,"|", angryNode.type,"--> ", angryNode.examinePerceptron(imgList[i]))
    #print(i,"|", michNode.type,"--> ", michNode.examinePerceptron(imgList[i]))
    #print(i,"|", sadNode.type,"--> ", sadNode.examinePerceptron(imgList[i]))
