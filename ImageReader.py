from Image import Image

# Parse training file and its correct-answer file
def parse(fileN, facitN):
    fileName = fileN
    facitName = facitN
    imgList = []

    # Make sure the file can be opened, otherwise, closes the program.
    try:
        with open(fileName) as f:
            content = f.readlines()
            f.close();
    except:
        sys.exit("Check your trainingfile and try again")

    pixel_list = []
    # Reads the file containing the images with pixels and the values.
    # Skips the rows that starts with # and empty rows.
    # Divides every pixel value with 31 to get a value between 0 and 1.
    for row in range(0, len(content)):
        if ((content[row][0:1] != '#') and (content[row] != '\n')):
            if (content[row][0:5] == "Image"):
                row = row + 1
                for i in range(row, row + 20):
                    pixel_list.extend([float(x)/31 for x in content[i].split(' ')])
                row = row + 20

    # Make sure the file can be opened, otherwise, closes the program.
    try:
        with open(facitName) as f:
            contentFacit = f.readlines()
    except:
        sys.exit("Check your facit and try again")

    facitList = []
    # Parse the fil containing the correct answer of the images.
    # Skips the rows that starts with # and empty rows.
    # Get the facit result as a list filled with int.
    for row in range(len(contentFacit)):  # Går igenom hela contentFacit
        if ((contentFacit[row][0:1] != '#') and (contentFacit[row] != '\n')):
            facitList.extend([int(contentFacit[row].split()[1])])

    # Build the image objects
    for i in range(len(facitList)):
        currImg = Image(pixel_list[i * 400:i * 400 + 400], facitList[i])
        imgList.append(currImg)

    return imgList

# Parse the test-file and builds a list with image objects
def parseTest(fileN):
    fileName = fileN
    imgList = []
    # Make sure the file can be opened, otherwise, closes the program.
    try:
        with open(fileName) as f:
            content = f.readlines()
            f.close();
    except:
        sys.exit("Check your trainingfile and try again")

    # Reads the file containing the images with pixels and the values.
    # Skips the rows that starts with # and empty rows.
    # Divides every pixel value with 31 to get a value between 0 and 1.
    pixel_list = []
    for row in range(0, len(content)):
        if ((content[row][0:1] != '#') and (content[row] != '\n')):
            if (content[row][0:5] == "Image"):
                row = row + 1
                for i in range(row, row + 20):
                    pixel_list.extend([float(x)/31 for x in content[i].split(' ')])
                row = row + 20

    # Build the image objects
    for i in range(int((len(pixel_list))/400)):
        currImg = Image(pixel_list[i * 400:i * 400 + 400], -1)
        imgList.append(currImg)

    return imgList
