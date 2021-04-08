from graphics import *

def main():
    win = GraphWin()
    win.setCoords(0.0, 0.0, 10.0, 10.0)
#    shape = Circle(Point(50,50), 20)
    shape = Rectangle(Point(1.0, 1.0), Point(3.0, 3.0))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        shape1 = shape.clone()
        dx = p.getX()-c.getX()
        dy = p.getY()-c.getY()
        shape1.setFill("violet")
        shape1.draw(win)
        shape1.move(dx,dy)

    msg = Text(Point(5.0,5.0), "Click again to quit")
    msg.draw(win)
    win.getMouse()
    win.close()
main()
