from graphics import *
from button import Button

class Calculator:
    # This class implements a simple calculator GUI
 
    def __init__(self):
        # create the window for the calculator
        win = GraphWin("calculator")
        win.setCoords(0,0,6,7)
        win.setBackground("slategray")
        self.win = win
        self.__createButtons()
        self.__createDisplay()

    def __createButtons(self):
        # create list of buttons
        # start with all the standard sized buttons
        # bSpecs gives center coords and label of buttons
        bSpecs = [(2,1,'0'), (3,1,'.'),
                  (1,2,'1'), (2,2,'2'), (3,2,'3'), (4,2,'+'), (5,2,'-'),
                  (1,3,'4'), (2,3,'5'), (3,3,'6'), (4,3,'*'), (5,3,'/'),    
                  (1,4,'7'), (2,4,'8'), (3,4,'9'), (4,4,'<-'), (5,4,'C')] 
        self.buttons = []
        for (cx, cy, label) in bSpecs:
            self.buttons.append(Button(self.win, Point(cx,cy), 0.75, 0.75, label))
        # create the larger '=' button"
        self.buttons.append(Button(self.win, Point(4.5,1), 1.75, 0.75, "="))
        # activate all buttons
        for b in self.buttons:
            b.activate()

    def __createDisplay(self):
        bg = Rectangle(Point(0.5, 5.5), Point(5.5, 6.5))
        bg.setFill('white')
        bg.draw(self.win)
        text = Text(Point(3, 6), "")
        text.draw(self.win)
        text.setFace("courier")
        text.setStyle("bold")
        text.setSize(16)
        self.display = text
    
    def getButton(self):
        # waits for a button to be clicked and returns the label of the button that was clicked
        while True:
            p = self.win.getMouse()
            for b in self.buttons:
                if b.clicked(p):
                    return b.getLabel()  # method exit

    def processButton(self, key):
        # updates the display of the calculator for press of this key
        text = self.display.getText()
        if key == 'C':
            self.display.setText("")
        elif key == '<-':
            # backspace, slice off the last character.
            self.display.setText(text[:-1])
        elif key == '=':
            try:
                result = eval(text)
            except:
                result = 'ERROR'
            self.display.setText(text + key)

    def run(self):
        while True:
            key = self.getButton()
            self.processButton(key)

if __name__ == '__main__':
    # first create a calculator object
    theCalc = Calculator()
    # Now call the calculator's run method
    theCalc.run()











         
              
