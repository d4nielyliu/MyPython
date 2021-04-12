from graphics import *
from random import random

def printIntro():
    print("This program evaluates pi via Monte Carlo techniques")
    
def simDarts(n):
    win = GraphWin("", 400, 400)
    win.setCoords(-1.2, -1.2, 1.2, 1.2)
    hits = 0    

    for i in range(n):
        pt = getDarts()
        if hitTarget(pt):
           hits = hits + 1
        else:
           hits = hits
    return hits
           
def getDarts():
    x = 2 * random() -1
    y = 2 * random() -1
    pt = Point(x, y)
    return pt

def hitTarget(pt):
    x = pt.getX()
    y = pt.getY()
    if (x**2+y**2) <= 1:
       return True
    else:
       return False


def getPi(hits, n):
    pi = 4 * (hits/n)
    return pi


def main():
    printIntro()
    n = eval(input("Please enter the number of simulation (n > 500): "))
    h = simDarts(n)
    pi = getPi(h, n)
    print("Pi = ", pi)
    

main()
