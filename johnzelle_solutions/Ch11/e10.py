def inputSeq(n):
    mySeq = []
    for i in range(2,n+1):
        mySeq.append(i)
    return mySeq



def main():

    n = eval(input("Please enter a positive integer: "))
    mySeq = inputSeq(n)
#    print(mySeq)
    
    new =[]
#    while len(mySeq) !=0
    new.append(mySeq[0])
    print(new)
    mySeq.remove(mySeq[0])
    print(mySeq)
    for i in mySeq:
        if i % new[-1] == 0:
           mySeq.remove(i)
    print(mySeq)
         
    new.append(mySeq[0])
    print(new)
    mySeq.remove(mySeq[0])
    print(mySeq)
    for i in mySeq:
        if i % new[-1] == 0:
           mySeq.remove(i)
    print(mySeq)
        
    new.append(mySeq[0])
    print(new)
    mySeq.remove(mySeq[0])
    print(mySeq)
    for i in mySeq:
        if i % new[-1] == 0:
           mySeq.remove(i)
    print(mySeq)

    new.append(mySeq[0])
    print(new)
    mySeq.remove(mySeq[0])
    print(mySeq)
    for i in mySeq:
        if i % new[-1] == 0:
           mySeq.remove(i)
    print(mySeq)

main()
