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
    print("This program sorts student grade information by GPA")
    filename = input("Please enter the name of the data file: ")
    data = readStudents(filename)
    data.sort(key=Student.gpa)
    data.reverse()
    filename = input("Please a name for the output file: ")
    writeStudents(data, filename)
    print("The data has been written to", filename)

if __name__ == '__main__': main()
