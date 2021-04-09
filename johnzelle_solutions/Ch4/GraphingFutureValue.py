from graphics import *


def main():
    print("This program calculates the future value")
    print("of a 10-year investment.")
    
    principal = eval(input("Please enter your initial principal: "))
    apr = eval(input("Please enter your APR: "))

    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground ("white")

    Text(Point(20, 230), ' 0.0K').draw(win)
    Text(Point(20, 180), ' 2.5K').draw(win)
    Text(Point(20, 130), ' 5.0K').draw(win)
    Text(Point(20, 80), ' 7.5K').draw(win)
    Text(Point(20, 30), ' 10.0K').draw(win)

    height = principal * 0.02
    bar = Rectangle(Point(40, 230), Point(65, 230-height))
    bar.setFill("red")
    bar.setWidth(2)
    bar.draw(win)



    for i in range(1,11):
        principal = principal * (1 + apr/100)
        dx = 40+i*25
        dy = principal * 0.02
        bar = Rectangle(Point(dx, 230), Point(dx+25, 230-dy))
        bar.setFill('red')
        bar.setWidth(2)
        bar.draw(win)
        print("The value for ", i , "th year is: ", principal)

    print("The value in 10 years is: ", principal)

    input("Press <Enter> to quit")
    win.close()    


main() 
      


        
