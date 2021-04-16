from cube import *

def main():
    r = eval(input("What is the side length of your cube?  "))
    c1 = Cube(r)
    A = c1.surfaceArea()
    V = c1.volume()
    print("The volume of your sphere is {0:0.4f}.".format(V))
    print("The surface area of your sphere is {0:0.4f}.".format(A))

main()
