fileName = "training.txt"

with open(fileName) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like \n at the end of each line
#content = [x.strip() for x in content]


tempPixel_list = []
tempNumber = 0
for row in range(0, len(content)):
    if((content[row][0:1] != '#') and (content[row] != '\n')):
        if(content[row][0:5] == "Image"):
            tempNumber = content[row][5:]
            row = row + 1
            #print(content[row].split())
            for i in range(row, row+20):
                tempPixel_list.append([int(j) for j in content[i].split()])
            row = row + 20

# Parsa facit fil
facitList = []


# Bygga ImageObj
imageNr = 0
pixelList = []
pixelList.extend(tempPixel_list[imageNr*20+imageNr:imageNr*20+imageNr+20]) # Parse pixelRows x to x + 20
# 0-19, 20-39


print(pixelList.reshape(-1))

#img = []
#for i in range(0, 20):
#    for j in range(0, 20):
#        img.append(pixelList[0][i][j])

#print(len(img))