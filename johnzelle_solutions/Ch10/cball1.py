from math import *

def main():
    angle = eval(input("Please enter the launch angle (in degrees): "))
    vel = eval(input("Please enter the initial velocity: "))
    h0 = eval(input("Please enter the initial height: "))
    time = eval(input("Please enter the time interval between position calculations: "))

    theta = radians(angle)

    xpos = 0.0
    ypos = h0
    xvel = vel * cos(theta)
    yvel = vel * sin(theta)

    while ypos >= 0.0:
        xpos = xpos + time * xvel
        yvel1 = yvel - time *9.8
        ypos = ypos + time * (yvel + yvel1)/2.0
        yvel = yvel1   
    print("\nDistance traveled: {0:0.1f} meters.".format(xpos))


main()
