#cube.py
import math

class Cube:
      
    def __init__(self, length):
        self.length = length
    
    def getLength(self):
        return self.length

    def surfaceArea(self):
        return 6*self.length**2

    def volume(self):
        return self.length**3
