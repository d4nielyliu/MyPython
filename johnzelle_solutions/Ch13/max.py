def findtheLargestNumber(array):
    # Write your code here.
    target = []
    n = len(array)
    maxi = array[0]
    for i in range(1,n):
        if maxi <= array[i]:
            maxi = array[i]
    target.append(maxi)
    array.remove(maxi)
    return target, array

def findThreelargestNumbers(array):
    t1, a1 = findtheLargestNumber(array)
    t2, a2 = findtheLargestNumber(a1)
    t3, a3 = findtheLargestNumber(a2)
    return [t1[0],t2[0],t3[0]]

    




