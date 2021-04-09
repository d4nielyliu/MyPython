def main():

    print("This program generates computer usernames.\n")

    first = input("Please enter your first name (all lowercase): ")
    last = input("Please enter your last name (all lowercase): ")

    uname = first[0] + last[:7]

    print("Your username is: ", uname)

main()
