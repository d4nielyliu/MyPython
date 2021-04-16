#button.py
from graphics import *

class CButton:
    
    """ A button is a labled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked (p) method
    returns true if the button is active and p is inside it."""

    def __init__(self, win, center, radius, label):
#    def __init__(self, win, center, width, height, label):
        """ Creates a circle button, eg:
        qb = Button(myWin, centerPoint, radius, 'Quit') """

#        w, h = width/2.0, height/2.0
        x, y = center.getX(), center.getY()
        self.center = Point(x,y)
        self.radius = radius
        self.xmax, self.xmin = x+radius, x-radius
        self.ymax, self.ymin = y+radius, y-radius
#        p1 = Point(self.xmin, self.ymin)
#        p2 = Point(self.xmax, self.ymax)
#        self.rect = Rectangle(p1,p2)
#        self.rect.setFill('lightgray')
#        self.rect.draw(win)
        self.circ = Circle(self.center, self.radius)
        self.circ.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()


    def clicked(self, p):
        "Returns true if button active and p is inside"
        return (self.active and 
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.xmax)

    def getLabel(self):
        "Returns the label string of this button"
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
#        self.rect.setWidth(2)
        self.circ.setWidth(2)
        self.active = True

    def deactivate(self):
        "Sets this button to 'active'."
        self.label.setFill('darkgrey')
#        self.rect.setWidth(1)
        self.circ.setWidth(1)
        self.active = False

    def update(self, win, label):
        self.label.undraw()
        self.label = Text(self.center, label)
        self.active = False
        self.label.draw(win)
