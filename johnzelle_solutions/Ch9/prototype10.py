from random import random

def main():
    n = eval(input("Please enter the number of simulations: "))

    hits = 0
 
    for i in range(n):
        x = 2* random() - 1
        y = 2* random() - 1
        print(x,y)
        if (x**2+y**2)<=1:
           hits = hits + 1
        else:
           hits = hits

    pi = 4*(hits/n)
    print("Pi = ",pi)

main()
