from PIL import Image as image
from ast import literal_eval as toTuple
import WindowMgr, time, win32api, win32con
import pyautogui, os, shutil, glob
from PIL import ImageDraw
import tkinter as tk



'''
oldImg = image.open('field.jpg', 'r')
yCoordinate = 0
for r in range(0,4):ui
    xCoordinate = 0
    for c in range(0,5):
        newImg = image.new('RGB', (int(oldImg.width/5),int(oldImg.height/4)))
        for y in range(0, newImg.height):
            for x in range(0, newImg.width):
                try:
                    newImg.putpixel((x,y), oldImg.getpixel((xCoordinate + x, yCoordinate + y)))
                except:
                    pass
        newImg.save('ChopChop/trylang{0}-{1}.jpg'.format(xCoordinate,yCoordinate))
        xCoordinate += newImg.width
    yCoordinate += newImg.height



'''
#Load waypoint per levels on Mission Planner
def loader():
    mgr = WindowMgr.WindowMgr()
    mgr.find_window_wildcard('Mission Planner .*')
    mgr.set_foreground()
    mgr.set_size()
    click(90,50)
    click(1117,260)

def loadLvl2():
    loader()
    pyautogui.typewrite('level2.waypoints')
    pyautogui.press('enter')
def loadLvl3():
    loader()
    pyautogui.typewrite('level3.waypoints')
    pyautogui.press('enter')
def loadLvl4():
    loader()
    pyautogui.typewrite('level4.waypoints')
    pyautogui.press('enter')
def loadLvl5():
    loader()
    pyautogui.typewrite('level5.waypoints')
    pyautogui.press('enter')
def loadAll():
    loader()
    pyautogui.typewrite('cont.waypoints')
    pyautogui.press('enter')


def click(x,y):
    time.sleep(.5)
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def createMap(dimensions):
    print('creating map with {0}x{1} dimensions.'.format(dimensions[0],dimensions[1]))
    csvFile = open('output.csv','r')
    csvData = csvFile.read().split('\n')
    csvFile.close()
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
    #print(newSize)
    levelColor = list()
    
    for x in range(2,6):
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
                
    print(levelColor)
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
                else:
                    testLevel = 3
                testImage = image.open('fileBank/{0}'.format(filenames[fileIndex]))
                for r in range(0, testImage.height):
                    for c in range(0, testImage.width):
                        try:
                            outMap.putpixel((xCoordinate + c, yCoordinate + r), levelColor[testLevel])
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
                testImage = image.open('fileBank/{0}'.format(filenames[fileIndex]))
                for r in range(0, testImage.height):
                    for c in range(0, testImage.width):
                        try:
                            outMap.putpixel((xCoordinate + c, yCoordinate + r), levelColor[testLevel])
                        except:
                            pass
                fileIndex += 1
                xCoordinate -= int(newSize[0]/dimensions[0])
        yCoordinate += int(newSize[1]/dimensions[1])
    outMap.save('results\map.png')
    """    
    img = image.open('results\map.png')
    draw = ImageDraw.Draw(img) 
    j=0
    for i in range(dimensions[1]):
        j = j + img.height/dimensions[1]
        draw.line((0,j, img.width,j), fill=(0,0,0,128))
    k=0
    for i in range(dimensions[0]):
        k = k + img.width/dimensions[0]
        draw.line((k,0, k,img.height), fill=(0,0,0,128))
    img = img.resize((600,400))
    img.save("test\map.png")
    """
    img = image.open('results\map.png')
    draw = ImageDraw.Draw(img) 
    j=0
    for i in range(dimensions[1]):
        draw.line((0,j, img.width,j), fill=(0,0,0,128), width=10)
        j = j + img.height/dimensions[1]       
    k=0
    for i in range(dimensions[0]):
        draw.line((k,0, k,img.height), fill=(0,0,0,128), width=10)
        k = k + img.width/dimensions[0]

    img.save('results\map.png')

def createMap2(dimensions):
    print('creating map with {0}x{1} dimensions.'.format(dimensions[0],dimensions[1]))
    csvFile = open('output.csv','r')
    csvData = csvFile.read().split('\n')
    csvFile.close()
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
    levelColor = list()
    
    for x in range(2,6):
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
    levelColor.append((255,255,255))                
    print(levelColor)
    outMap = image.new('RGB', newSize)

    fileIndex = 0
    yCoordinate = 0
    for y in range(dimensions[1]):
        if y % 2 == 0:
            xCoordinate = 0
            for x in range(dimensions[0]):
                if levelData[fileIndex] == 'Level 2':
                    testLevel = 0
                else:
                    testLevel = 4
                testImage = image.open('fileBank/{0}'.format(filenames[fileIndex]))
                for r in range(0, testImage.height):
                    for c in range(0, testImage.width):
                        try:
                            outMap.putpixel((xCoordinate + c, yCoordinate + r), levelColor[testLevel])
                        except:
                            pass
                fileIndex += 1
                xCoordinate += int(newSize[0]/dimensions[0])
        else:
            xCoordinate = int((newSize[0]/dimensions[0])*(dimensions[0] - 1))
            for x in range(dimensions[0]):
                if levelData[fileIndex] == 'Level 2':
                    testLevel = 0
                else:
                    testLevel = 4
                testImage = image.open('fileBank/{0}'.format(filenames[fileIndex]))
                for r in range(0, testImage.height):
                    for c in range(0, testImage.width):
                        try:
                            outMap.putpixel((xCoordinate + c, yCoordinate + r), levelColor[testLevel])
                        except:
                            pass
                fileIndex += 1
                xCoordinate -= int(newSize[0]/dimensions[0])
        yCoordinate += int(newSize[1]/dimensions[1])
    outMap.save('results\map2.png')

    img = image.open('results\map2.png')
    draw = ImageDraw.Draw(img) 
    j=0
    for i in range(dimensions[1]):
        draw.line((0,j, img.width,j), fill=(0,0,0,128), width=10)
        j = j + img.height/dimensions[1]       
    k=0
    for i in range(dimensions[0]):
        draw.line((k,0, k,img.height), fill=(0,0,0,128), width=10)
        k = k + img.width/dimensions[0]
       
    img.save('results\map2.png')


def createMap3(dimensions):
    print('creating map with {0}x{1} dimensions.'.format(dimensions[0],dimensions[1]))
    csvFile = open('output.csv','r')
    csvData = csvFile.read().split('\n')
    csvFile.close()
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
    levelColor = list()
    
    for x in range(2,6):
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
    levelColor.append((255,255,255))                
    print(levelColor)
    outMap = image.new('RGB', newSize)

    fileIndex = 0
    yCoordinate = 0
    for y in range(dimensions[1]):
        if y % 2 == 0:
            xCoordinate = 0
            for x in range(dimensions[0]):
                if levelData[fileIndex] == 'Level 3':
                    testLevel = 1
                else:
                    testLevel = 4
                testImage = image.open('fileBank/{0}'.format(filenames[fileIndex]))
                for r in range(0, testImage.height):
                    for c in range(0, testImage.width):
                        try:
                            outMap.putpixel((xCoordinate + c, yCoordinate + r), levelColor[testLevel])
                        except:
                            pass
                fileIndex += 1
                xCoordinate += int(newSize[0]/dimensions[0])
        else:
            xCoordinate = int((newSize[0]/dimensions[0])*(dimensions[0] - 1))
            for x in range(dimensions[0]):
                if levelData[fileIndex] == 'Level 3':
                    testLevel = 1
                else:
                    testLevel = 4
                testImage = image.open('fileBank/{0}'.format(filenames[fileIndex]))
                for r in range(0, testImage.height):
                    for c in range(0, testImage.width):
                        try:
                            outMap.putpixel((xCoordinate + c, yCoordinate + r), levelColor[testLevel])
                        except:
                            pass
                fileIndex += 1
                xCoordinate -= int(newSize[0]/dimensions[0])
        yCoordinate += int(newSize[1]/dimensions[1])
    outMap.save('results\map3.png')

    img = image.open('results\map3.png')
    draw = ImageDraw.Draw(img) 
    j=0
    for i in range(dimensions[1]):
        draw.line((0,j, img.width,j), fill=(0,0,0,128), width=10)
        j = j + img.height/dimensions[1]       
    k=0
    for i in range(dimensions[0]):
        draw.line((k,0, k,img.height), fill=(0,0,0,128), width=10)
        k = k + img.width/dimensions[0]
     
    img.save('results\map3.png')


def createMap4(dimensions):
    print('creating map with {0}x{1} dimensions.'.format(dimensions[0],dimensions[1]))
    csvFile = open('output.csv','r')
    csvData = csvFile.read().split('\n')
    csvFile.close()
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
    levelColor = list()
    
    for x in range(2,6):
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
    levelColor.append((255,255,255))                
    print(levelColor)
    outMap = image.new('RGB', newSize)

    fileIndex = 0
    yCoordinate = 0
    for y in range(dimensions[1]):
        if y % 2 == 0:
            xCoordinate = 0
            for x in range(dimensions[0]):
                if levelData[fileIndex] == 'Level 4':
                    testLevel = 2
                else:
                    testLevel = 4
                testImage = image.open('fileBank/{0}'.format(filenames[fileIndex]))
                for r in range(0, testImage.height):
                    for c in range(0, testImage.width):
                        try:
                            outMap.putpixel((xCoordinate + c, yCoordinate + r), levelColor[testLevel])
                        except:
                            pass
                fileIndex += 1
                xCoordinate += int(newSize[0]/dimensions[0])
        else:
            xCoordinate = int((newSize[0]/dimensions[0])*(dimensions[0] - 1))
            for x in range(dimensions[0]):
                if levelData[fileIndex] == 'Level 4':
                    testLevel = 2
                else:
                    testLevel = 4
                testImage = image.open('fileBank/{0}'.format(filenames[fileIndex]))
                for r in range(0, testImage.height):
                    for c in range(0, testImage.width):
                        try:
                            outMap.putpixel((xCoordinate + c, yCoordinate + r), levelColor[testLevel])
                        except:
                            pass
                fileIndex += 1
                xCoordinate -= int(newSize[0]/dimensions[0])
        yCoordinate += int(newSize[1]/dimensions[1])
    outMap.save('results\map4.png')

    img = image.open('results\map4.png')
    draw = ImageDraw.Draw(img) 
    j=0
    for i in range(dimensions[1]):
        draw.line((0,j, img.width,j), fill=(0,0,0,128), width=10)
        j = j + img.height/dimensions[1]       
    k=0
    for i in range(dimensions[0]):
        draw.line((k,0, k,img.height), fill=(0,0,0,128), width=10)
        k = k + img.width/dimensions[0]     
    img.save('results\map4.png')
    
def createMap5(dimensions):
    print('creating map with {0}x{1} dimensions.'.format(dimensions[0],dimensions[1]))
    csvFile = open('output.csv','r')
    csvData = csvFile.read().split('\n')
    csvFile.close()
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
    levelColor = list()
    
    for x in range(2,6):
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
    levelColor.append((255,255,255)) #blank white                
    print(levelColor)
    outMap = image.new('RGB', newSize)

    fileIndex = 0
    yCoordinate = 0
    for y in range(dimensions[1]):
        if y % 2 == 0:
            xCoordinate = 0
            for x in range(dimensions[0]):
                if levelData[fileIndex] == 'Level 5':
                    testLevel = 3
                else:
                    testLevel = 4
                testImage = image.open('fileBank/{0}'.format(filenames[fileIndex]))
                for r in range(0, testImage.height):
                    for c in range(0, testImage.width):
                        try:
                            outMap.putpixel((xCoordinate + c, yCoordinate + r), levelColor[testLevel])
                        except:
                            pass
                fileIndex += 1
                xCoordinate += int(newSize[0]/dimensions[0])
        else:
            xCoordinate = int((newSize[0]/dimensions[0])*(dimensions[0] - 1))
            for x in range(dimensions[0]):
                if levelData[fileIndex] == 'Level 5':
                    testLevel = 3
                else:
                    testLevel = 4
                testImage = image.open('fileBank/{0}'.format(filenames[fileIndex]))
                for r in range(0, testImage.height):
                    for c in range(0, testImage.width):
                        try:
                            outMap.putpixel((xCoordinate + c, yCoordinate + r), levelColor[testLevel])
                        except:
                            pass
                fileIndex += 1
                xCoordinate -= int(newSize[0]/dimensions[0])
        yCoordinate += int(newSize[1]/dimensions[1])
    outMap.save('results\map5.png')

    img = image.open('results\map5.png')
    draw = ImageDraw.Draw(img) 
    j=0
    for i in range(dimensions[1]):
        draw.line((0,j, img.width,j), fill=(0,0,0,128), width=10)
        j = j + img.height/dimensions[1]       
    k=0
    for i in range(dimensions[0]):
        draw.line((k,0, k,img.height), fill=(0,0,0,128), width=10)
        k = k + img.width/dimensions[0]       
    img.save('results\map5.png') 

def Map(dimensions, mapType):
    print('creating {0} map with {1}x{2} dimensions.'.format(mapType,dimensions[0],dimensions[1]))
    csvFile = open('output.csv','r')
    csvData = csvFile.read().split('\n')
    csvFile.close()
    
    mapFileName = ''
    if mapType == 'Level 2':
        mapFileName = 'results\map2.png'
    elif mapType == 'Level 3':
        mapFileName = 'results\map3.png'
    elif mapType == 'Level 4':
        mapFileName = 'results\map4.png'
    elif mapType == 'Level 5':
        mapFileName = 'results\map5.png'
    else:
        mapFileName = 'results\map.png'
        
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
    img = ImageDraw.Draw(img) 
    j=0
    for i in range(dimensions[1]):
        draw.line((0,j, img.width,j), fill=(0,0,0,128))
        j = j + img.height/dimensions[1]
    k=0
    for i in range(dimensions[0]):
        draw.line((k,0, k,img.height), fill=(0,0,0,128))
        k = k + img.width/dimensions[0] 
    img.save(mapFileName)   

#copy images from one folder to another
def copy(dir):
    print(dir)
    src_dir = dir
    dst_dir = "fileBank"
    for jpgfile in glob.iglob(os.path.join(src_dir, "*.jpg")):
        shutil.copy(jpgfile, dst_dir)

'''
try:
    planner = win32gui.FindWindow(None, '.*Mission Planner .*')
    win32gui.ShowWindow(planner,5)
    win32gui.SetForegroundWindow(planner)
except:
    planner = None

if(planner):
    print("FOUND")
else:
    print("NOT FOUND")
'''




