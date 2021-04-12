from random import randrange

def printIntro():
    print("This program simulates the random walk")

def oneRandWalk():
    a = randrange(1,3)
    return a

def avgSteps(n):
    totTravel = 0
    for i in range(1000):
        steps = nRandWalk(n)
        totTravel = totTravel + steps
    if totTravel == 0:
       avgTravel = 0
    else:
       avgTravel = totTravel/1000
    return avgTravel

def nRandWalk(n):
    nsteps = 0
    for i in range(n):
        x = oneRandWalk()
        if x == 1:
           nsteps = nsteps + 1
        elif x==2:
           nsteps = nsteps - 1
    return nsteps


def main():
    printIntro()
    n = eval(input("Please enter the number of steps: "))
    avgTravel = avgSteps(n)
    print("The object will travel an average of", avgTravel, "based on the MC simulation.")


main()
