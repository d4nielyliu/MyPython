def main():
    sum = 0.0
    count = 0
    moredata = "yes"

    while moredata[0] == "y":
        x = eval(input("Please enter a number >> "))
        sum = sum + x
        count = count + 1
        moredata = input("Do you have more numbers (yes or no)? ")
    print("\nThe average of the number is", sum/count)


main()
