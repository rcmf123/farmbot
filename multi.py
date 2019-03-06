import gui
from multiprocessing import Process
from PIL import Image as image
from PIL import ImageDraw


def createMap(dimensions, mapType):
    print('creating {0} map with {1}x{2} dimensions.'.format(mapType,dimensions[0],dimensions[1]))
    csvFile = open('output.csv','r')
    csvData = csvFile.read().split('\n')
    csvFile.close()
    
    mapFileName = ''
    if mapType == 'Level 2':
        mapFileName = 'map2.png'
    elif mapType == 'Level 3':
        mapFileName = 'map3.png'
    elif mapType == 'Level 4':
        mapFileName = 'map4.png'
    elif mapType == 'Level 5':
        mapFileName = 'map5.png'
    else:
        mapFileName = 'map.png'
        
    filenames = list()
    levelData = list()
    for x in range(len(csvData)):
        if(csvData[x] != ''):
            splitData = csvData[x].split(',')
            filenames.append(splitData[0])
            levelData.append(splitData[1])
        else:
            break
    firstImage = image.open('fileBank/{0}'.format(filenames[0]))
    newSize = (firstImage.width*dimensions[0],firstImage.height*dimensions[1])
    firstImage.close()
    print(newSize)
    levelColor = list()
    '''
    for x in range(2,7):
        try:
            testFile = open('calibrationInfo/level{0}.txt'.format(x))
            levelColor.append(toTuple(testFile.read()))
            testFile.close()
        except:
            if x == 2:
                levelColor.append((150,170,85))
            elif x == 3:
                levelColor.append((120,151,58))
            elif x == 4:
                levelColor.append((89,132,40))
            elif x == 5:
                levelColor.append((58,113,18))
            elif x == 6:
                levelColor.append((255,255,255))
                
    print(levelColor)
    '''
    levelColor.append ((255, 105, 97))
    levelColor.append ((255, 179, 71))
    levelColor.append ((253, 253, 150))
    levelColor.append ((119, 221, 119))
    levelColor.append ((255, 255, 255))
    
    outMap = image.new('RGB', newSize)

    fileIndex = 0
    yCoordinate = 0
    for y in range(dimensions[1]):
        if y % 2 == 0:
            xCoordinate = 0
            for x in range(dimensions[0]):
                if levelData[fileIndex] == 'Level 2':
                    testLevel = 0
                elif levelData[fileIndex] == 'Level 3':
                    testLevel = 1
                elif levelData[fileIndex] == 'Level 4':
                    testLevel = 2
                elif levelData[fileIndex] == 'Level 5':
                    testLevel = 3

                if mapType == 'Level 2':
                    if testLevel != 0:
                        testLevel = 4
                elif mapType == 'Level 3':
                    if testLevel != 1:
                        testLevel = 4
                elif mapType == 'Level 4':
                    if testLevel != 2:
                        testLevel = 4
                elif mapType == 'Level 5':
                    if testLevel != 3:
                        testLevel = 4
                
                testImage = image.open('fileBank/{0}'.format(filenames[fileIndex]))
                for r in range(0, testImage.height):
                    for c in range(0, testImage.width):
                        try:
                            calcPixel = list()
                            testPixel = testImage.getpixel((c, r))
                            levelPixel = levelColor[testLevel]
                            if mapType != 'All Level' and testLevel != 4:
                                levelPixel = testPixel
                            for x in range(3):
                                pigment = testPixel[x] + levelPixel[x]
                                pigment /= 2
                                calcPixel.append(int(pigment))
                            newPixel = (calcPixel[0],calcPixel[1],calcPixel[2])
                            outMap.putpixel((xCoordinate + c, yCoordinate + r), newPixel)
                        except:
                            pass
                fileIndex += 1
                xCoordinate += int(newSize[0]/dimensions[0])
        else:
            xCoordinate = int((newSize[0]/dimensions[0])*(dimensions[0] - 1))
            for x in range(dimensions[0]):
                if levelData[fileIndex] == 'Level 2':
                    testLevel = 0
                elif levelData[fileIndex] == 'Level 3':
                    testLevel = 1
                elif levelData[fileIndex] == 'Level 4':
                    testLevel = 2
                else:
                    testLevel = 3

                if mapType == 'Level 2':
                    if testLevel != 0:
                        testLevel = 4
                elif mapType == 'Level 3':
                    if testLevel != 1:
                        testLevel = 4
                elif mapType == 'Level 4':
                    if testLevel != 2:
                        testLevel = 4
                elif mapType == 'Level 5':
                    if testLevel != 3:
                        testLevel = 4
                        
                testImage = image.open('fileBank/{0}'.format(filenames[fileIndex]))
                for r in range(0, testImage.height):
                    for c in range(0, testImage.width):
                        try:
                            calcPixel = list()
                            testPixel = testImage.getpixel((c, r))
                            levelPixel = levelColor[testLevel]
                            if mapType != 'All Level' and testLevel != 4:
                                levelPixel = testPixel
                            for x in range(3):
                                pigment = testPixel[x] + levelPixel[x]
                                pigment /= 2
                                calcPixel.append(int(pigment))
                            newPixel = (calcPixel[0],calcPixel[1],calcPixel[2])
                            outMap.putpixel((xCoordinate + c, yCoordinate + r), newPixel)
                        except:
                            pass
                fileIndex += 1
                xCoordinate -= int(newSize[0]/dimensions[0])
        yCoordinate += int(newSize[1]/dimensions[1])
    outMap.save(mapFileName)
    
    img = image.open(mapFileName)
    draw = ImageDraw.Draw(img) 
    j=0
    for i in range(dimensions[1]):
        print(img.height)
        j = j + img.height/dimensions[1]
        draw.line((0,j, img.width,j), fill=(0,0,0,128))
    k=0
    for i in range(dimensions[0]):
        print(img.width)
        k = k + img.width/dimensions[0]
        draw.line((k,0, k,img.height), fill=(0,0,0,128))
    print((testImage.width,testImage.height))
    newImg = img.resize((testImage.width,testImage.height))    
    newImg.save(mapFileName)
"""    
if __name__=='__main__':

    p1 = Process(target=createMap, args=(dimensions, 'a')) # create a process object p1
    p1.start()                   # starts the process p1
    p2 = Process(target=createMap, args=(dimensions, 'Level 2'))
    p2.start()
    p3 = Process(target=createMap, args=(dimensions, 'Level 3'))
    p3.start()
    p4 = Process(target=createMap, args=(dimensions, 'Level 4'))
    p4.start()
    p5 = Process(target=createMap, args=(dimensions, 'Level 5'))
    p5.start()

dimensions = [5, 6]
#createMap(dimensions, 'Level 2')
#createMap(dimensions, 'Level 3')
#createMap(dimensions, 'Level 4')
#createMap(dimensions, 'Level 5')
createMap(dimensions, 'Level 1')
"""
