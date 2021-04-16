from sphere import *

def main():
    r = eval(input("What is the radius of your sphere?  "))
    s1 = Sphere(r)
    A = s1.surfaceArea()
    V = s1.volume()
    print("The volume of your sphere is {0:0.4f}.".format(V))
    print("The surface area of your sphere is {0:0.4f}.".format(A))

main()
