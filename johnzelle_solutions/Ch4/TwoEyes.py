from graphics import *

def main():
    
    leftEye = Circle(Point(80,50), 5)
    leftEye.setFill('yellow')
    leftEye.setOutline('red')
    
    rightEye = leftEye.clone()
    rightEye.move(20,0)

    windows = GraphWin('Two Eyes')
    leftEye.draw(windows)
    rightEye.draw(windows)



main()
