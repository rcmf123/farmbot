#####GENERATE WAYPOINTS DEPENDING ON LEVEL
from pathlib import Path
import sys, string, os
def wpGen(filename):
    
    os.system(r"GreenReader.exe")#Run greenreader.exe
    
    waypoints = [] #array
    with open(filename, 'r') as infile: #open waypoint file
        for line in infile: 
            waypoints.append(line)  #store each line of text in an array

    #combine image results with waypoints
    with open('output.csv', 'r') as infile, open('results\wptestoutput.waypoints', 'w') as outfile: 
        n=2 #start at 3rd index or [2] of the line
        for line in infile:
            outfile.write(line.strip() +","+waypoints[n]) #separate csv data and waypoint with comma
            n+=1 #next line
            #outfile.write(waypoints[n])
            #n+=1        

    Path('results\level2.waypoints').touch() #create blank text file
    Path('results\level3.waypoints').touch()
    Path('results\level4.waypoints').touch()
    Path('results\level5.waypoints').touch()
    Path('results\cont.waypoints').touch()
    f = open("results\wptestoutput.waypoints","r+")
    one = open("results\level2.waypoints","r+")
    two = open("results\level3.waypoints","r+")
    three = open("results\level4.waypoints","r+")
    four = open("results\level5.waypoints","r+")
    cont = open("results\cont.waypoints","r+")
    d = f.readlines()
    f.seek(0)
    one.write('QGC WPL 110 \n')
    one.write(waypoints[1]) #write home point which is stored in second index of array
    two.write('QGC WPL 110 \n')
    two.write(waypoints[1]) #write home point which is stored in second index of array
    three.write('QGC WPL 110 \n')
    three.write(waypoints[1]) #write home point which is stored in second index of array
    four.write('QGC WPL 110 \n')
    four.write(waypoints[1]) #write home point which is stored in second index of array
    cont.write('QGC WPL 110 \n')
    cont.write(waypoints[1]) #write home point which is stored in second index of array   
    for i in d:
        if 'Level 2' in i:
            one.write(i.split(',')[2])
        elif 'Level 3' in i:
            two.write(i.split(',')[2])
        elif 'Level 4' in i:
            three.write(i.split(',')[2])
        elif 'Level 5' in i:
            four.write(i.split(',')[2])
    for i in d:
        if 'Level ' in i:
            cont.write(i.split(',')[2])
    f.close()

####INSERT LAT, LONG INTO ARRAYS
def getLatLong():
    global coords
    global coords1
    global coords2
    global coords3
    global coords4

    coords = []
    coords1 = []
    coords2 = []
    coords3 = []
    coords4 = []
    #extract long and lat
    with open('results\level2.waypoints', 'r') as infile: 
        next(infile)
        n = 0
        for line in infile:
            coords1.append([line.split()[8],line.split()[9]])
    # extract long and lat
    with open('results\level3.waypoints', 'r') as infile: 
        next(infile)
        n = 0
        for line in infile:
            coords2.append([line.split()[8],line.split()[9]])
    # extract long and lat
    with open('results\level4.waypoints', 'r') as infile: 
        next(infile)
        n = 0
        for line in infile:
            coords3.append([line.split()[8],line.split()[9]])                    
    # extract long and lat
    with open('results\level5.waypoints', 'r') as infile: 
        next(infile)
        n = 0
        for line in infile:
            # 8=lat; 9=long
            coords4.append([line.split()[8],line.split()[9]])
    # extract long and lat        
    with open('results\cont.waypoints', 'r') as infile: 
        next(infile)
        n = 0
        for line in infile:
            coords.append([line.split()[8],line.split()[9]])


try:
    getLatLong()
except:
    pass

####HAVERSINE FUNCTION
import math
def haversine(lat1, lon1, lat2, lon2):

      R = 6372.8 

      dLat = math.radians(lat2 - lat1)
      dLon = math.radians(lon2 - lon1)
      lat1 = math.radians(lat1)
      lat2 = math.radians(lat2)

      a = math.sin(dLat/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin(dLon/2)**2
      c = 2*math.asin(math.sqrt(a))

      return R * c * 1000

####DISTANCE
def distance():
    distance = 0
    i = 0
    while i < len(coords) - 1:
        distance = distance + haversine(float(coords[i][0]), float(coords[i][1]), float(coords[i+1][0]), float(coords[i+1][1]))
        i += 1
    #print("TOTAL DISTANCE: " + str(distance) +" meters")
    return distance
    
def distance1():
    distance = 0
    i = 0
    while i < len(coords1) - 1:
        distance = distance + haversine(float(coords1[i][0]), float(coords1[i][1]), float(coords1[i+1][0]), float(coords1[i+1][1]))
        i += 1
    #print("TOTAL DISTANCE: " + str(distance) +" meters")
    return distance

def distance2():
    distance = 0
    i = 0
    while i < len(coords2) - 1:
        distance = distance + haversine(float(coords2[i][0]), float(coords2[i][1]), float(coords2[i+1][0]), float(coords2[i+1][1]))
        i += 1
    #print("TOTAL DISTANCE: " + str(distance) +" meters")
    return distance

def distance3():
    distance = 0
    i = 0
    while i < len(coords3) - 1:
        distance = distance + haversine(float(coords3[i][0]), float(coords3[i][1]), float(coords3[i+1][0]), float(coords3[i+1][1]))
        i += 1
    #print("TOTAL DISTANCE: " + str(distance) +" meters")
    return distance

def distance4():
    distance = 0
    i = 0
    while i < len(coords4) - 1:
        distance = distance + haversine(float(coords4[i][0]), float(coords4[i][1]), float(coords4[i+1][0]), float(coords4[i+1][1]))
        i += 1
    #print("TOTAL DISTANCE: " + str(distance) +" meters")
    return distance

#########TIME-DISTANCE-SPEED#########
def time(level):
    speed = 5  #constant; depends on the drone setup
    if len(coords) == 0:
        raise Exception("empty list")
    
    if level == 0:
        time = distance()/speed
        time = time + (3 * (len(coords) -1))
    elif level == 2:
        time = distance1()/speed
        time = time + (3 * (len(coords1) -1))
    elif level == 3:
        time = distance2()/speed
        time = time + (3 * (len(coords2) -1))
    elif level == 4:
        time = distance3()/speed
        time = time + (3 * (len(coords3) -1))
    elif level == 5:
        time = distance4()/speed
        time = time + (3 * (len(coords4) -1))       

    return time      



####export
from fpdf import FPDF
import plot
 
def export():
    plot.plot_bar_x(2)
    pdf = FPDF()
    pdf.set_font("Arial", size=12)
    imagefiles = ["results\map.png", "results\map2.png", "results\map3.png", "results\map4.png", "results\map5.png"]
    label = ["All levels", "Level 2", "Level 3", "Level 4", "Level 5"]
    data = [['Flight Path', 'Total Distance', 'Time Travelled'],
            ['Continuous', str(distance()), str(time(0))],
            ['Per level total', str(distance1()+distance1()+distance2()+distance3()+distance4()), str(time(2)+time(3)+time(4)+time(5))],
            ['Level 2', str(distance1()), str(time(2))],
            ['Level 3', str(distance2()), str(time(3))],
            ['Level 4', str(distance3()), str(time(4))],
            ['Level 5', str(distance4()), str(time(5))]            
            ]
    pdf.add_page()
    pdf.image("results\graph.png", x=10, y=8, w=200)
    pdf.ln(160)
    col_width = pdf.w / 4.5
    row_height = pdf.font_size + 1
    for row in data:
        for item in row:
            pdf.cell(col_width, row_height*1,
                     txt=item, border=1)
        pdf.ln(row_height*1)

 
    i = 0
    j = 0 
    for one_image in imagefiles:
        pdf.add_page()
        pdf.image(one_image, x=10 + j, y=8, w=100)
        pdf.set_font("Arial", 'B', size=12)
        pdf.ln(65)  # move 85 down
        pdf.cell(200, 10, txt=label[i], ln=1)
        print(label[i])
        print(i)
        i = i + 1
        j + 200
    pdf.output("results\export.pdf")
 

def delete():
    import os
    import glob

    files = glob.glob('fileBank/*')
    for f in files:
        os.remove(f)
