def sumN(n):
    Sum = 0
    for i in range(1,n+1):
        Sum = Sum + i

    return Sum

def sumNCubes(n):
    Sum3 = 0
    for i in range(1,n+1):
        Sum3 = Sum3 + i**3

    return Sum3



def main():
    num = eval(input("Please enter a natural number: "))
    s1 = sumN(num)
    print("The sum from 1 to ",num, "is: ", s1) 

    s3 = sumNCubes(num)
    print("The sum of the cubes of first ",num, "natural numbers is: ", s3) 
    


main()
