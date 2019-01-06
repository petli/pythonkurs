# Rita kvadrat

from turtle import *

for i in range(4):
    forward(200)
    left(360 / 4)


# Funktion för att rita figur

def kvadrat():
    for i in range(4):
        forward(200)
        left(360 / 4)

for i in range(4):
    kvadrat()
    left(45)

# Rita godtycklig liksidig figur

def liksidig_figur(sidor):
    vinkelsumma = 180.0 * (sidor - 2)
    hornvinkel = vinkelsumma / sidor
    svangvinkel = 180.0 - hornvinkel
    for i in range(sidor):
        forward(200)
        left(svangvinkel)

for i in range(3, 8):
    liksidig_figur(i)
