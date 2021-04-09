def main():

    principal = eval(input("Please enter the principal: "))
    apr = eval(input("Please enter the annualized interest rate: "))

    p = principal
    year = 0
    interest = 0.0

    while principal >= 0.5 * p:
        year = year + 1
        interest = p * apr * 0.01
        p = p + interest

    print(p)
    print(year)




main()
