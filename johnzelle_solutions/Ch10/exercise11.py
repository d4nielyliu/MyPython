from card import Card
from random import random

def main():
    n = 20
    for i in range (n):
        x = int(random() * 13) + 1
        y = int(random() * 4)
        suit = ['d', 's', 'h', 'c']
        card = Card(x, suit[y])
        print(card)
        print(card.BJValue())
        print()
main()
