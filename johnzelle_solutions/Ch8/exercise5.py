from math import *

def main():
    
    n = eval(input("Please enter an integer (n>=2): "))

    i = 2 
    np = 1
    b = 0

    while i <= int(sqrt(n)):
        if n%i == 0:
           b = 1
           np = i
#           print(np, "divides", n)
#           print(n, "is no prime number.")
        else:
           b = 0
        
        i = i + 1

    if b==1:
       print(n, "is no prime number.")
       print(np, "divides", n)
    else:
       print(n, "is a prime number.") 

main()
        
