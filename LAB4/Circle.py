from PIL import Image, ImageDraw
import sys

class drawOnImage:
    def __init__(self):
        self.img = Image.open("Data\USA.png")
        self.draw = ImageDraw.Draw(self.img)

    def drawCircle(self):
        self.draw.ellipse((50, 50, 100, 100), fill=(255,0,0,255)) # da capire ed estendere

    def save(self):
        #del self.draw
        self.img.save("USA2.png", "PNG")