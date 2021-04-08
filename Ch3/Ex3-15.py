import math

def main():
    print("This program calculates pi.")

    n = eval(input("Please enter an integer: "))
    Pi=0.0

    for i in range(1, n, 1):
        Pi= Pi+(4.0/(2*i-1))*(-1)**(i+1)

    print("Pi = ", Pi)

    Percent_diff = abs(Pi-math.pi)/math.pi*100

    print("The precent difference is ", Percent_diff, "%")





main()
