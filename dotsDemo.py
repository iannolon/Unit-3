
#IanNolon
#3/1/18
#dotsDemo.py - how to use loops with graphics

from ggame import *

RADIUS = 2

maroon = Color(0x800000,1)

dot = CircleAsset(RADIUS,LineStyle(1,maroon),maroon)

for i in range (16): #putting a row of dots
    for j in range(16):
        Sprite(dot,(10 + (RADIUS*2+10) * i,10+ (RADIUS*2+10) * j))

App().run()

