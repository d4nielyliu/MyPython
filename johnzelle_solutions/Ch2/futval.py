def main():
    print("This program calculates the future value")
    print("of a 10-year investment.")
    
    principal = eval(input("Please enter your initial principal: "))
    apr = eval(input("Please enter your APR: "))

    for i in range(10):
        principal = principal * (1 + apr/100)
        print("The value for ", i , "th year is: ", principal)

    print("The value in 10 years is: ", principal)


main() 
      


        
