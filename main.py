import ImageReader
import Node

fileName = "training.txt"
facitName = "training-facit.txt"

imgList = ImageReader.parse(fileName,facitName)

happyNode = Node.Node(0.5, 1)
#angryNode = Node.Node(0.5, 4)
#michNode = Node.Node(0.5, 3)
#sadNode = Node.Node(0.5, 2)

happyNode.teachPerceptron(imgList[0:199])
#angryNode.teachPerceptron(imgList[0:199])
#michNode.teachPerceptron(imgList[0:199])
#sadNode.teachPerceptron(imgList[0:199])

happyNode.examinePerceptron(imgList[200:300])
#angryNode.examinePerceptron(imgList[200:300])
#michNode.examinePerceptron(imgList[200:300])
#sadNode.examinePerceptron(imgList[200:300])
