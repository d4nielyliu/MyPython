def main():
    sum = 0.0
    count = 0
    x = eval(input("Please enter a number (negative to quit) >> "))

    while x >= 0:
        sum = sum + x
        count = count + 1
        x = eval(input("Please enter a number (negative to quit) >> "))
    print("\nThe average of the number is", sum/count)


main()
