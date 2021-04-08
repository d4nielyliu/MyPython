from graphics import *

def main():
    win = GraphWin("Draw a triangle")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    msg = Text(Point(5, 0.5), "Click on three points")
    msg.draw(win)

    p1 = win.getMouse()
    p2 = win.getMouse()
    p3 = win.getMouse()

    p1.draw(win)
    p2.draw(win)
    p3.draw(win)

    triangle = Polygon(p1, p2, p3)
    triangle.setFill("red")
    triangle.setOutline("black")
    triangle.draw(win)


    msg.setText("Click anywhere on it")
    win.getMouse()
    win.close()

main()
