from PIL import Image, ImageDraw

def drawLines(map)
    img = Image.open(map)
    draw = ImageDraw.Draw(img) 

    j=0
    for i in range(4):
        print(img.height)
        j = j + img.height/4
        draw.line((0,j, img.width,j), fill=(0,0,0,128))
    k=0
    for i in range(5):
        print(img.width)
        k = k + img.width/5
        draw.line((k,0, k,img.height), fill=(0,0,0,128))
        
    img.save(map)
