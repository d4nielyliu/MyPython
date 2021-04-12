from random import random

def printIntro():
    print("THis program simulates a game of racquetbal between two")
    print('players called "A" and "B". The ablities of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving. Player A always")
    print("has the first serve.")

def getInputs():
    a = eval(input("What is the prob. player A wins a serve? "))
    b = eval(input("What is the prob. player B wins a serve? "))
    n = eval(input("How many games to simulate? "))
    return a, b, n

def simNGames_25(n, probA, probB):
    winsA = 0
    winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame_25(probA, probB, n)
        if scoreA > scoreB:
           winsA = winsA + 1
        else:
           winsB = winsB + 1    
    return winsA, winsB

def simOneGame_25(probA, probB, n):
    scoreA = 0
    scoreB = 0
    serving = whoServes(n)
    while not gameOver_25(scoreA, scoreB):
        if serving == "A":
           if random() < probA:
              scoreA = scoreA + 1
           else:
              serving = "B"
              scoreB = scoreB + 1
        else:
           if random() < probB:
              scoreB = scoreB + 1
           else:
              serving = "A"
              scoreA = scoreA + 1
    return scoreA, scoreB 

def whoServes(n):
    if n % 2 == 0:
        return "A"
    else:
        return "B"


def gameOver_25(a, b):
    if a > 23 or b > 23:
        if abs(a-b) >= 2:
            return True
        else:
            return False
    else:
        return False


def simNGames_15(n, probA, probB):
    winsA = 0
    winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame_15(probA, probB, n)
        if scoreA > scoreB:
           winsA = winsA + 1
        else:
           winsB = winsB + 1    
    return winsA, winsB

def simOneGame_15(probA, probB, n):
    scoreA = 0
    scoreB = 0
    serving = whoServes(n)
    while not gameOver_15(scoreA, scoreB):
        if serving == "A":
           if random() < probA:
              scoreA = scoreA + 1
           else:
              serving = "B"
        else:
           if random() < probB:
              scoreB = scoreB + 1
           else:
              serving = "A"
    return scoreA, scoreB 


def gameOver_15(a, b):
    if a > 13 or b > 13:
        if abs(a-b) >= 2:
            return True
        else:
            return False
    else:
        return False





def printSummary(winsA, winsB):
    n = winsA + winsB 
    print("\nGames simulated:", n)
    print("Wins for A: {0} ({1:0.1%})".format(winsA, winsA/n))
    print("Wins for B: {0} ({1:0.1%})".format(winsB, winsB/n))






def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA_15, winsB_15 = simNGames_15(n, probA, probB)
    winsA_25, winsB_25 = simNGames_25(n, probA, probB)
    printSummary(winsA_15, winsB_15)
    printSummary(winsA_25, winsB_25)




main()    
