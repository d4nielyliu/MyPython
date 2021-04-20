from gpa import Student, makeStudent

def readStudents(filename):
    infile = open(filename, 'r')
    students = []
    for line in infile:
        students.append(makeStudent(line))
    infile.close()
    return students

def writeStudents(students, filename):
    outfile = open(filename, 'w')
    for s in students:
        print("{0}\t{1}\t{2}\t{3}".format(s.getName(), s.getHours(), s.getQPoints(), s.gpa()), file = outfile)
    outfile.close()

def main():
    print("This program sorts student grade information")
    filename = input("Please enter the name of the data file: ")
    data = readStudents(filename)
#    data.sort(key=Student.gpa)
#    data.reverse()
#    filename1 = input("Please a name for the output file for the data sorted by GPA: ")
#    writeStudents(data, filename1)
#    print("The data sorted by GPA has been written to", filename1)
#    data.sort(key=Student.getHours)
#    data.reverse()
#    filename2 = input("Please a name for the output file for the data sorted by HOURS: ")
#    writeStudents(data, filename2)
#    print("The data sorted by GPA has been written to", filename2)

    while True:
        x = (input('Type "GPA", "name", or "credits" >>>  '))
        if x == 'GPA':
            data.sort(key=Student.gpa)
            s = "_(GPA)"
            break
        elif x == 'name': 
            data.sort(key=Student.getName)
            s = "_(name)"
            break 
        elif x == 'credits':
            data.sort(key=Student.getQPoints)
            s = "_(credits)"
            break
        else:
            print("Please try again.")
    
    #filename = input("enter a name for the outputfile: ")
    filename = "gpa" + s + ".py"
    writeStudents(data, filename)
    print("The data has been written to", filename)

if __name__ == '__main__': main()


