#IanNolon
#1/7/18
#olympic.py

from ggame import *

blue = Color(0x0000FF,1)
yellow = Color(0xFFFF00,1)
black = Color(0x000000,1)
green = Color(0x00FF00,1)
red = Color(0xFF0000,1) 
white = Color(0xFFFFFF,1)

blueOutline = LineStyle(1,blue)
yellowOutline = LineStyle(1,yellow)
blackOutline = LineStyle(1,black)
greenOutline = LineStyle(1,green)
redOutline = LineStyle(1,red)
whiteOutline = LineStyle(1,white)

whiteCircle = CircleAsset(60,whiteOutline,white)
blueCircle = CircleAsset(70,blueOutline,blue)
yellowCircle = CircleAsset(70,yellowOutline,yellow)
blackCircle = CircleAsset(70,blackOutline,black)
greenCircle = CircleAsset(70,greenOutline,green)
redCircle = CircleAsset(70,redOutline,red)
text = TextAsset('RUSSIA', fill = red, style = 'bold 40pt Times')

Sprite(blueCircle,(70,60))
Sprite(whiteCircle,(80,70))
Sprite(yellowCircle,(120,140))
Sprite(whiteCircle,(130,150))
Sprite(blackCircle,(160,60))
Sprite(whiteCircle,(170,70))
Sprite(greenCircle,(220,140))
Sprite(whiteCircle,(230,150))
Sprite(redCircle,(270,60))
Sprite(whiteCircle,(280,70))

Sprite(text,(160,350))

App().run()
