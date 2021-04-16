class Student:
    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def getQPoints(self):
        return self.qpoints

    def gpa(self):
        self.gpa = self.qpoints / self.hours
        return self.gpa

    def addGrade(self, gradePoint, credits):
        self.hours = float(self.hours) + float(credits)
        self.qpoints = self.qpoints + (gradePoint * credits)

    def addGradeLetter(self, GPA):
        if 90.0<=GPA<=100.0:
           return "A"
        elif 80.0<=GPA<90.0:
           return "B"
        elif 70.0<=GPA<80.0:
           return "C"
        elif 60.0<=GPA<70.0:
           return "D"
        else:
           return "F"

def makeStudent(infoStr):
    #inforStr is a tap-separated line: name hours getQPoints
    #returns a corresponding Student object
    name, hours, qpoints = infoStr.split("\t")
    return Student(name, hours, qpoints)

def main():
    new = makeStudent("Smith, Frank	0	0")
    x, y = eval(input("Input gradepoint and credits, separated by a comma: "))
    new.addGrade(x, y)
    print(new.getHours(), new.getQPoints())
    print(new.gpa())
    print(new.addGradeLetter(x))

main()
