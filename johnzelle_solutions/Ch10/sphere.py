#sphere.py
import math

class Sphere:
      
    def __init__(self, radius):
        self.radius = radius
    
    def getRadius(self):
        return self.radius

    def surfaceArea(self):
        r = self.radius
        return 4*math.pi*r**2

    def volume(self):
        r = self.radius
        return (4.0/3.0)*math.pi*r**3
