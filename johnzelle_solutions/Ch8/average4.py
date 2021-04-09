def main():
    sum = 0.0
    count = 0
    xStr = input("Please enter a number (<Enter> to quit) >> ")

    while xStr != "":
        sum = sum + eval(xStr)
        count = count + 1
        xStr = input("Please enter a number (<Enter> to quit) >> ")
    print("\nThe average of the number is", sum/count)


main()
