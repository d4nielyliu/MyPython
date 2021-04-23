from random import *

class Player:
    def __init__(self, prob):
        self.prob = prob
        self.score = 0

    def winsServe(self):
        return random() <= self.prob
    
    def incScore(self):
        self.score = self.score + 1
     
    def getScore(self):
        return self.score


class RBallGame:
    def __init__(self, probA, probB):
        self.playerA = Player(probA)
        self.playerB = Player(probB)
        self.server = self.PlayerA
  
    def play(self):
        while not self.isOver():
            if self.server.winsServe():
                self.server.incScore()
            else:
                self.changeServer()

    def isOver(self):
        a, b = self.getScores()
        return a == 15 or b == 15 or (a == 7 and b == 0) or (b == 7 and a == 0)
                
    def changeServer(self):
        if self.server == self.playerA:
            self.server == self.playerB
        else:
            self.server == self.playerA

    def getScores(self):
        return self.playerA.getScore(), self.playerB.getScore()


class SimStatus:
    def __init__(self):
        self.winsA = 0
        self.winsB = 0
        self.shutsA = 0
        self.shutsB = 0
    
    def update(self,aGame):
        a, b = aGame.getScores()
        if a > b:
            self.winsA = self.winsA + 1
            if b == 0:
                self.shutsA = self.shutsA + 1
        else:
            self.winsB = self.winsB + 1
            if a == 0:
                self.shutsB = self.shutsB + 1

    def printReport(self):
        # print a nicely formatted report
        n = self.winsA + self.winsB
        print("Summary of", n, "games:\n")
        print("          wins (% total)  shoutouts (% wins) ")
        print("--------------------------------------------")
        self.prinLine("A", self.winsA, self.shutsA, n)
        self.prinLine("B", self.winsB, self.shutsB, n)

    def printLine(self, label, wins, shuts, n):
        template = "Player {0}:{1:5}  ({2:5..1%})  {3:11}    ({4})"
        if wins == 0:
            shutStr = "-----"
        else:
            shutStr = "{0:4.1%}".format(float(shuts)/wins)
        print(template.format(label, wins, float(wins)/n, shuts, shutStr))

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




def main():
    printIntro()
    probA, probB, n = getInputs()
    # play the game
    stats = SimStats()
    for i in range(n):
        theGame = RBallGame(probA, probB)
        theGame.play()
        status.update(theGame)
    # print the results
    status.printReport()


main()
input("\nPress <Enter> to quit")




