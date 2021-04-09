def syr(x):
    if x % 2 == 0:
        syrX = x/2
    elif x % 2 == 1:
        syrX = 3 * x + 1
    return syrX


def main():
    
    x = eval(input("Please enter an non-negative integer: "))
    print(x)

    while x > 1:
        syr_x = syr(x)
        x = syr_x
        print(syr_x)


main()


