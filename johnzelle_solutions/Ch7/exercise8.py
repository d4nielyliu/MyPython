def main():
    age = eval(input("Please enter your age: "))
    citizen = eval(input("How long have you been a US citizen: "))

    if citizen >= 9:
       if age >= 30:
          print("You are eligible to serve as a U.S. Senator.")
       elif 25<= age < 30:
          print("You are not eligible to serve as a U.S. Senator, but eligible to serve as a representative of the House")
       else:
          print("You are not eligible to serve as a U.S. Senater or a representative of the House")

    elif 7<= citizen < 9:
       if age >=25:
          print("You are not elibigle to sever as a U.S. Senator, but eligible to serve as a representative of the House") 
       else:
          print("You are not eligible to serve as a U.S. Senater or a representative of the House")

    else:
       print("You are not eligible to serve as a member of congress at all!")


main()
       
