from math import *

def quadSol(x, y, z):
    discROOT = sqrt(y**2-4.0*x*z)
    root1 = (-y + discROOT)/(2.0*x)
    root2 = (-y - discROOT)/(2.0*x)
    return root1, root2


def main():
    print("This programs solves a quadratic equation.")

    a, b, c = eval(input("Please input three coefficients(a,b,c): "))

    delta = b**2-4.0*a*c
    if delta >= 0:
       r1, r2 = quadSol(a, b, c)
       print("\nThe solutions are: ", r1, r2)


main()
  

    
