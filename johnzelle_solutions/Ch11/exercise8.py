def isin(myList, x):
    for i in myList:
        if i == x:
            return True

def removeDuplicates(myList):
    newList = []
    for i in myList:
        if not isin(newList, i):
            newList.append(i)
    return newList


def main():
    List = [1,1,2,3,5,8]*3
 
    print(removeDuplicates(List))

main()
