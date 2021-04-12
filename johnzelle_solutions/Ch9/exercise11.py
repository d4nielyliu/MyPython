from random import randrange

def printIntro():
    print("This program evaluates the probability of rolling") 
    print("six-of-a-kind in a single roll of five six-sided dice")
    
def FiveOfAKind():
    a, b, c, d, e = simOneRoll()
    if a == b == c == d == e:
        return True
    else:
        return False

def simOneRoll():
    dice = []
    for i in range (5):
        x = randrange(1, 5)
        dice.append(x)
    return dice
    


def main():
    printIntro()
    n = eval(input("How many simulations would you like to perform? "))
    five_to_one = 0
    for i in range(n):
        simOneRoll()
        if FiveOfAKind():
           five_to_one = five_to_one + 1
        else:
           five_to_one = five_to_one

    P = five_to_one/n

    print("The probability of rolling six-of-a-kind is: ", P)   

main()

