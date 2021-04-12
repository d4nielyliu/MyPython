from random import randrange

def main():
    printIntro()
    n = eval(input("How many hands should I simulate? >> "))
    busts = simNHands(n)
    printSummary(busts, n)

def printIntro():
    print("This program is designed to simulate (n) games of blackjack")
    print('and will return the probability of the dealer "busting" or')
    print("going beyond 21.")
    print()

def simNHands(n):
    busts = 0
    for i in range(n):
        if simOneHand():
           busts = busts + 1
    return busts

def simOneHand():
    x = simOneCard()
    y = simOneCard()
    hand = x + y

    while hand < 17:
        if hasAce(x) is True:
            if hand <= 10:
                x = 11
                hand = hand + 10
            else:
                x = 1


        if hasAce(y) is True:
            if hand <= 10:
                y = 11
                hand = hand + 10
            else:
                y = 1
        z = simOneCard()
        hand = hand + z

    if hand > 21:
        #bust
        return True
    else:
        return False

def simOneCard():
    x = randrange(1, 13)
    if x == 11 or x == 12 or x == 13:
        x = 10
        return x
    else:
        return x

def hasAce(x):
    if x == 1:
        return True
    else:
        return False

def printSummary(busts, n):
    print()
    print("The dealer has a {0:0.1%} chance of busting.".format(busts/n))

main()

