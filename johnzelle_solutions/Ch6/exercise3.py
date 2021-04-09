from math import *


def sphereArea(radius):
    area = 4 * pi * (radius*radius)
    return area
def sphereVolume(radius):
    volume = 4/3 * pi * (radius ** 3)
    return volume

def main():
    r = (eval(input("Input a value for the radius: ")))
    a = sphereArea(r)
    v = sphereVolume(r)
    print("A sphere with radius", r, "has volume", round(v, 3), "and surface area", round(a, 3),".")

main()
    

