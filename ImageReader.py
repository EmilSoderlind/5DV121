from Image import Image


def parse(fileN, facitN): # Parse Learning-file + facit-file
    fileName = fileN
    facitName = facitN
    imgList = []
    try:
        with open(fileName) as f:
            content = f.readlines()
            f.close();
    except:
        sys.exit("Check your trainingfile and try again")

    pixel_list = []
    # tempNumber = 0
    # Räcker med for row in range (längd av fil) om vi vill börja från 0
    for row in range(0, len(content)):
        if ((content[row][0:1] != '#') and (content[row] != '\n')):
            if (content[row][0:5] == "Image"):
                row = row + 1
                for i in range(row, row + 20):
                    pixel_list.extend([float(x)/31 for x in content[i].split(' ')])
                row = row + 20

    # Parsa facit fil
    try:
        with open(facitName) as f:
            contentFacit = f.readlines()
    except:
        sys.exit("Check your facit and try again")

    facitList = []
    # Räcker med for row in range (18) om vi vill börja från 0
    # Get the facit result as a list filled with int.

    for row in range(len(contentFacit)):  # Går igenom hela contentFacit
        if ((contentFacit[row][0:1] != '#') and (contentFacit[row] != '\n')):
            facitList.extend([int(contentFacit[row].split()[1])])

    # Bygga ImageObj
    for i in range(len(facitList)):
        # print("index: ", i*400, " To: ", i*400+399)
        currImg = Image(pixel_list[i * 400:i * 400 + 400], facitList[i])
        imgList.append(currImg)

    return imgList

def parseTest(fileN): #Parse a test-file without facit
    fileName = fileN

    imgList = []

    try:
        with open(fileName) as f:
            content = f.readlines()
            f.close();
    except:
        sys.exit("Check your trainingfile and try again")

    pixel_list = []
    # tempNumber = 0
    # Räcker med for row in range (längd av fil) om vi vill börja från 0
    for row in range(0, len(content)):
        if ((content[row][0:1] != '#') and (content[row] != '\n')):
            if (content[row][0:5] == "Image"):
                row = row + 1
                for i in range(row, row + 20):
                    pixel_list.extend([float(x)/31 for x in content[i].split(' ')])
                row = row + 20

    # Bygga ImageObj
    for i in range(int((len(pixel_list))/400)):
        # print("index: ", i*400, " To: ", i*400+399)
        currImg = Image(pixel_list[i * 400:i * 400 + 400], -1)
        imgList.append(currImg)

    return imgList
