from gpa import Student, makeStudent
from graphics import *
from button import Button

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
    

def sort(filename, x, y):
    data = readStudents(filename)
    while True:
        if x == 'GPA':
            data.sort(key=Student.gpa)
            s = "_(GPA)"
            if y == 'D':
                data.reverse()  
            break
        elif x == 'name': 
            data.sort(key=Student.getName)
            s = "_(name)"
            if y == 'D':
                data.reverse() 
            break 
        elif x == 'credits':
            data.sort(key=Student.getQPoints)
            s = "_(credits)"
            if y == 'D':
                data.reverse() 
            break
        else:
            print("Please try again.")
    filename = "gpa" + s + ".txt"
    return filename, data


def main():

    infile = input("Please enter the name of data file: ")
    
    win = GraphWin("Sort Data File", 600, 600)
    win.setCoords(0,0,5,6)

    message = Text(Point(2.5,3), "This program sorts student grade information by GPA, name, or credits.\n Select the sorting method.")
    message.draw(win)            
 
    bSpecs = [(1,2,"GPA"), (2,2,"Name"), (3,2,"Credits"), (4,2,"Quit")]
    buttons = []
    for (cx, cy, label) in bSpecs:
        buttons.append(Button(win, Point(cx,cy), .75, .75, label))
    for b in buttons:
        b.activate()
    
    while True:
        click = win.getMouse()
        
        #return clicked for each button
        for b in buttons:
            if b.clicked(click):
                label = b.getLabel()
        while label != "Quit":
            if label == "GPA":
                x = "GPA"
                y = "D"
                break
            elif label == "Name":
                x = "name"
                y = "A"
                break
            elif label == "Credits":
                x = "credits"
                y = "D"
                break
            elif label == "Quit":
                break
            else:
                message.setText("Please try again.")
                click = win.getMouse()
        #call sort function, which should return filename
        outfile, data = sort(infile, x, y)
        writeStudents(data, outfile)
        outmessage = "The file has been printed to "+ outfile
        message.setText(outmessage)
        if label == "Quit":
            break


if __name__ == '__main__': 
    main()






    
