def main():

    x = eval(input("Please enter your credits: "))

    if x < 7:
        print('Freshman')
    elif 7 <= x <16:
        print('Sophomore')
    elif 16 <= x <26:
        print('Junior')
    elif x >= 26:
        print('Senior')
    else:
        print("Please print a positive number ")

main()
