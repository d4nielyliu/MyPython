from random import randrange

class MSDie:
      
    def __init__(self, sides):
        self.sides = sides
        self.value = 1

    def roll(self):
        self.value = randrange(1, self.sides+1)
        
    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value


def main():

    n = eval(input("Please the number of sides: "))
#    die1 = MSDie(n)
#    for i in range(10): 
#        die1.roll()
#        d = die1.getValue()
#        print(d)

    die2 = MSDie(13)
    print(die2.getValue())
    die2.setValue(8)
    print(die2.getValue())    

main()
