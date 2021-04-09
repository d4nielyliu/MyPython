from math import *

def main():
    
    n = eval(input("Please enter an integer (n>=2): "))

    i = 2 
#    np = 1
    b = 0

    for j in range(n):    
        while i <= int(sqrt(j)):
            if j%i == 0:
               b = 1
#               np = i
               return
            else:
               b = 0
            i = i + 1

        if b==1:
           print(j, "is no prime number.")
#           print(np, "divides", n)
        else:
           print(j, "is a prime number.") 

main()
        
