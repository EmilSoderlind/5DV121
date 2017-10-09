from Image import Image

fileName = "training.txt"
facitName = "training-facit.txt"
try:
    with open(fileName) as f:
        content = f.readlines()
        # you may also want to remove whitespace characters like \n at the end of each line
        #content = [x.strip() for x in content]
        f.close();
except:
    sys.exit("Check your trainingfile and try again")

pixel_list = []
#tempNumber = 0
#Räcker med for row in range (längd av fil) om vi vill börja från 0
for row in range(0, 313):
    if((content[row][0:1] != '#') and (content[row] != '\n')):
        if(content[row][0:5] == "Image"):
            #tempNumber = content[row][5:]
            row = row + 1
            #print(content[row].split())
            for i in range(row, row+20):
                pixel_list.extend([int(j) for j in content[i].split()])
            row = row + 20
            
#print (pixel_list)

# Parsa facit fil
try: 
    with open(facitName) as f:
        contentFacit = f.readlines()
except:
    sys.exit("Check your facit and try again")

facitList = []
#Räcker med for row in range (18) om vi vill börja från 0
#Get the facit result as a list filled with int.

for row in range(0, len(contentFacit)): # Går igenom hela contentFacit
    if((contentFacit[row][0:1] != '#') and (contentFacit[row] != '\n')):
        facitList.extend([int (contentFacit[row].split()[1])])
print (facitList)

# Bygga ImageObj
imageNr = 0
pixelList = []
pixelList.extend(pixel_list[imageNr*20+imageNr:imageNr*20+imageNr+20]) # Parse pixelRows x to x + 20
# 0-19, 20-39
#print (tempPixel_list)


#print(pixelList.reshape(-1))

#img = []
#for i in range(0, 20):
#    for j in range(0, 20):
#        img.append(pixelList[0][i][j])

#print(len(img))