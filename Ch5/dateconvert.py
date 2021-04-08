def main():
    
    dateStr = input("Enter a date (mm/dd/yyyy): ")
    monthStr, dayStr, yearStr = dateStr.split("/")

    monthList = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    monthNum = int(monthStr)



    month = monthList[monthNum-1]

#    print(month)
    print("The converted date is:", month, dayStr+",", yearStr)
    

main()


