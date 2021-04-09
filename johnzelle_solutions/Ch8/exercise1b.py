def main():
    print("Fibonacci sequence")

    n = eval(input("What number in Fibonacci sequence would you like to see: "))

    F_n =[1,1]

    for i in range(2,n):
        F_n.append(F_n[i-1]+F_n[i-2])

    print(F_n)

    for j in range(n):
        print(F_n[j])


main()
