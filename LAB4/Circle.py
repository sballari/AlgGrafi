from PIL import Image, ImageDraw, ImageColor
import sys

class drawOnImage:
    def __init__(self):
        self.img = Image.open("Data/USA.png")
        self.draw = ImageDraw.Draw(self.img)

    def drawCircle(self,coord):
        x = coord.getX()
        y = coord.getY()
        self.draw.ellipse((x-1, y-1, x+1, y+1), fill=(255,0,0,255))

    def drawLine(self,coord,coord2,color):
        x = coord.getX()
        y = coord.getY()
        x2 = coord2.getX()
        y2 = coord2.getY()
        self.draw.line((x,y,x2,y2), fill = ImageColor.getrgb(color))

    def save(self,name):
        #del self.draw
        self.img.save(name+".png", "PNG")