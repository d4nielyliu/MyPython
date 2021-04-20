def count(myList, x):
    counter = 0
    for i in myList:
        if i == x:
           counter = counter + 1
    return counter

def isin(myList, x):
    for i in myList:
        if i == x:
            return True

def index(myList, x):
    for i in range(len(myList)):
        if myList[i] == x:
           return i
           break
        
def reverse(myList):
    reverse = []
    for i in range(len(myList)):
        reverse.append(myList[-(i+1)])
    return reverse 

def sort(myList):
    newList = []
    for i in range (len(myList)):
        x = min(myList)
        newList.append(x)
        myList.remove(x)
    return newList


def main():
    L = [1,1,2,3,5,8]*3

    print("The count of L: ", count(L,3))
    print("X in L: ", isin(L, 1))
    print("Index of 5: ", index(L, 5))
    print("The reverse of L: ", reverse(L))
    print("Sort List: ", sort(L))


main()   
