from graphics import *
from math import *


def main():
    
    win = GraphWin("Five-click house", 600, 600)
    win.setCoords(0.0, 0.0, 20.0, 20.0)

    message = Text(Point(10.0, 18.0), "Click on 2 diagonal points to create the rectangular frame of your house.") 
    message.draw(win)

    p1 = win.getMouse()
    p1.draw(win)

    p2 = win.getMouse()
    p2.draw(win)  

    frame_width = abs(p2.getX()-p1.getX())
    frame = Rectangle(p1, p2)
    frame.draw(win)

    message.setText("Excellent! Click the top of the door frame.")

    door_center = win.getMouse()
    door_p1 = Point(door_center.getX()-0.1*frame_width, p1.getY())
    door_p2 = Point(door_center.getX()+0.1*frame_width, door_center.getY() )
    door_width = abs(door_p1.getX()-door_p2.getX())
    door = Rectangle(door_p1, door_p2)
    door.draw(win)

    message.setText("Now click to place a window.")
    
    win_center = win.getMouse()
    win_p1 = Point( win_center.getX()-0.25*door_width,  win_center.getY()-0.25*door_width)
    win_p2 = Point( win_center.getX()+0.25*door_width,  win_center.getY()+0.25*door_width)
    window = Rectangle(win_p1, win_p2)
    window.draw(win)

    message.setText("Finally, click the crown of the roof!")

    p3 = win.getMouse()
    p4 = Point(p1.getX(), p2.getY())
    
    peak = Polygon(p2, p4, p3)
    peak.draw(win)

    message.setText("Welocome home!")

    win.getMouse()
    win.close()

main()
