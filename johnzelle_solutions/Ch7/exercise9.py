def main():
    
    year = eval(input("Please enter a year (1982-2048): "))

    a = year % 19
    b = year % 4    
    c = year % 7
    d = (19*a + 24) % 30
    e = (2*b+4*c+6*d+5) % 7

    if 22+d+e<=31:
       print("The date of Easter is March", 22+d+e)
    else:
       print("The date of Easter is April", 31-(22+d+e))


main()
