def main():

    x1, x2, x3 = eval(input("Please enter three numbers: "))

    if x1 >= x2:
       if x1 >= x3:
          max =x1
       else:
          max = x3
    else:
       if x2 >= x3:
          max =x2
       else:
          max = x3

    print("The maximum value is: ", max)

main()

