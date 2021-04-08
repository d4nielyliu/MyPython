def main():
    print("This program calculates the future value")
    print("of a 10-year investment.")
    
    principal = eval(input("Please enter your initial principal: "))
    apr = eval(input("Please enter your APR: "))
    year = eval(input("Please enter the number of years for the investment: "))

    for i in range(year):
        principal = principal * (1 + apr/100)
        print("The value for ", i , "th year is: ", principal)

    print("The value in 10 years is: ", principal)


main() 
      
