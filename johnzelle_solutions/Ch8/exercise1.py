def main():
    print("Fibonacci sequence")

    n = eval(input("What number in Fibonacci sequence would you like to see: "))

    x = 1
    y = 0

    for i in range(n+1):
        z = x + y
        x = y
        y = z
        print(i+1,": ",z)
    


main()
