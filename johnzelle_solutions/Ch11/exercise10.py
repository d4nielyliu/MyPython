
def inputSeq(n):
    mySeq = []
    for i in range(2,n+1):
        mySeq.append(i)
    return mySeq


def main():
    n = eval(input("Please enter a positive integer: "))
    mySeq = inputSeq(n)

    
    new =[]
    while len(mySeq) !=0:
        new.append(mySeq[0])
        mySeq.remove(mySeq[0])
        for i in mySeq:
            if i % new[-1] == 0:
               mySeq.remove(i)
    print("The prime number betwwen 2 and", n, "is: ", new)


    
main()
