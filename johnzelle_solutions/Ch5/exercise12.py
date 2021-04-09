def main():
    
    print("This program calculates the future value\n", "of a 10-year investment.")

    principal = eval(input("Please enter the principal: "))
    apr = eval(input("Please enter the annual percentage rate: "))

    outfile = open("future.txt","w")
    print("{0:<} {1:>10}".format("Year", "Value"), file=outfile)
    print("----------------", file=outfile)
    print("{0:<}       ${1:<}.{2:0^2}".format(0, int(principal), int((principal%1)*100)), file=outfile)
 
    for i in range(9):
        principal = principal * (1 + apr/100)
        print("{0:<}       ${1:<}.{2:0^2}".format(i+1, int(principal), int((principal%1)*100)), file=outfile)

        

    print("----------------", file=outfile)









main()
