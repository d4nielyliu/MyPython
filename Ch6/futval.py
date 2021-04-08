from graphics import *

def createLabeledWindow():
    window = GraphWin("Investment Growth Chart", 320, 240)
    window.setBackground("white")
    window.setCoords(-1.75,-200,11.5,10400)
    Text(Point(-1, 0), '0.0K').draw(window)
    Text(Point(-1, 2500), '2.5K').draw(window)
    Text(Point(-1, 5000), '5.0K').draw(window)
    Text(Point(-1, 7500), '7.5K').draw(window)
    Text(Point(-1, 10000), '10.0K').draw(window)
    return window

def drawBar(window, year, height):
    bar = Rectangle(Point(year, 0), Point(year+1, height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(window)

def clickoff(window):
    message = Text(Point(5.50, 10000), "Click anywhere to quit")
    message.draw(window)
    window.getMouse()
    window.close()
   


def main():
    print("This program plots the growth of a 10-year investment.")
    
    principal = eval(input("Please enter the initial principal: "))
    apr = eval(input("Please enter the annual percentage rate: "))

    win = createLabeledWindow()
    drawBar(win,0,principal)

    for i in range(1,11):
        principal = principal * (1+0.01*apr)
        drawBar(win, i, principal)

#    message = Text(Point(5.50, 1000), "Click anywhere to quit")
#    message.draw(win)
#    win.getMouse()
#    win.close()
    clickoff(win)

main()
    
