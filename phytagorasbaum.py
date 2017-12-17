# Einstellungen
# Hoehe und Breite der Zeichenebene
blatt = 700
# Seitenlaenge des initialen Quadrates
quadrat = 80.0
# Abstand vom Rand
abstand = 80.0
# Ein Winkel im Dreieck
winkel  = 42.0
# Farben
quadratfarbe = "blue"
dreieckfarbe = "light blue"
hintergrund  = "white"

# Jetzt geht es los
import sys
import random
from tkinter import *
import math

iterations = 0
maxrecursion = 0

def pythagoras(can, a, b, wa, tiefe):

    global quadratfarbe
    global dreieckfarbe
    global iterations, maxrecursion

    x0 = a[0]
    y0 = a[1]
    x1 = b[0]
    y1 = b[1]
    if (math.fabs(x1-x0) + math.fabs(y1-y0) < 2):
        return
    
    iterations += 1
    if (tiefe > maxrecursion):
        maxrecursion = tiefe
    
    # draw rectangle
    h = y1 - y0
    b = x1 - x0
    x2 = x1 - h
    y2 = y1 + b
    x3 = x0 - h
    y3 = y0 + b
    can.create_polygon(x0, y0, x1, y1, x2, y2, x3, y3, fill=quadratfarbe)
       
    xx = (x2 - x3) * math.cos(wa)
    yy = (y2 - y3) * math.cos(wa)

    
    # now rotate xx/yy by wa
    dx = (xx * math.cos(wa)) - (yy * math.sin(wa))
    dy = (xx * math.sin(wa)) + (yy * math.cos(wa)) 

    xn = x3 + dx
    yn = y3 + dy
    can.create_polygon(x2, y2, xn, yn, x3, y3, fill=dreieckfarbe)
    can.update()

    pythagoras(can, (xn, yn), (x2, y2), wa, tiefe+1)
    pythagoras(can, (x3, y3), (xn, yn), wa, tiefe+1)
    


def zeichne(cansize, size, margin, angle):
    global hintergrund
    
    x0 = cansize/2.0
    x1 = cansize/2.0 + size
    y0 = margin
    y1 = margin

    top = Tk()
    
    canvas = Canvas(top, width=cansize, height=cansize, bg=hintergrund)
    canvas.pack()

    wa = angle * 2*math.pi / 360
    pythagoras(canvas, (x0, y0), (x1, y1), wa, 1)
    
    print ("Iterations: ", iterations)
    print ("Max Recursions: ", maxrecursion)

    top.mainloop()


zeichne(blatt, quadrat, abstand, winkel)
