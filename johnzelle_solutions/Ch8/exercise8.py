def main():
    m, n = eval(input("Please enter 2 numbers, separated by a comma: "))

    if m < n:
            y = n
            n = m
            m = y
            
    while m != 0:
            y = m
            m = n % m
            n = y
    print("The GCD is {}".format(n))

main()

