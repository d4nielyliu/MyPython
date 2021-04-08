def main():
    fname = input("Enter filename: ")
    infile = open(fname,"r")
#    data = infile.read()
#    print(data)
    for i in range(5):
        line = infile.readline()
        print(line[:-1])
   

main()
