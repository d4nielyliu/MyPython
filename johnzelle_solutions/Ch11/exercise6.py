from random import randrange

def shuffle(myList):
    newList = []
    for i in range(len(myList)):
        x = myList[randrange(0,len(myList))]
        newList.append(x)
        myList.remove(x)
    return newList

def main():
    L = [1,1,2,3,5,8]*4
    S = shuffle(L)
    print(S)

main()
