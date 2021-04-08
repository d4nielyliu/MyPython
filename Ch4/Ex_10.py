from graphics import *
from math import *


def main():
    win = GraphWin("Triangle Information", 400, 400)
    win.setCoords(0.0,0.0,10.0,10.0)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    Triangle = Polygon(p1, p2, p3)
    Triangle.setFill('red')
    Triangle.setOutline('red')
    Triangle.draw(win)

    dx_12 = p2.getX()-p1.getX()
    dy_12 = p2.getY()-p1.getY()
    l_12 = sqrt(dx_12**2+dy_12**2)

    dx_23 = p3.getX()-p2.getX()
    dy_23 = p3.getY()-p2.getY()
    l_23 = sqrt(dx_23**2+dy_23**2)

    dx_13 = p3.getX()-p1.getX()
    dy_13 = p3.getY()-p1.getY()
    l_13 = sqrt(dx_13**2+dy_13**2)



    s = (l_12+l_13+l_23)/2.0


    Area = sqrt(s*(s-l_12)*(s-l_23)*(s-l_13))

    print("The area of the triangle is: ", Area)

    msg = Text(Point(5.0,5.0), "Click again to quit")
    msg.draw(win)
    win.getMouse()
    win.close()

main()
