from graphics import *


def main():
    print("This program plots the future value of a 10-year investment.")
    
    principal = eval(input("Please enter your initial principal: "))
    apr = eval(input("Please enter your APR: "))

    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground ("white")
    win.setCoords(-1.75, -200, 11.5, 10400)

    Text(Point(-1, 0), ' 0.0K').draw(win)
    Text(Point(-1, 2500), ' 2.5K').draw(win)
    Text(Point(-1, 5000), ' 5.0K').draw(win)
    Text(Point(-1, 7500), ' 7.5K').draw(win)
    Text(Point(-1, 10000), ' 10.0K').draw(win)

#    height = principal * 0.02
    bar = Rectangle(Point(0, 0), Point(1, principal))
    bar.setFill("red")
    bar.setWidth(2)
    bar.draw(win)



    for i in range(1,11):
        principal = principal * (1 + apr/100)
#        dx = 1+i
#        dy = principal * 0.02
        bar = Rectangle(Point(i, 0), Point(i+1, principal))
        bar.setFill('red')
        bar.setWidth(2)
        bar.draw(win)
        print("The value for ", i , "th year is: ", principal)

    print("The value in 10 years is: ", principal)

    input("Press <Enter> to quit")
    win.close()    


main() 
      


        
