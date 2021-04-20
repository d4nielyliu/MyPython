from math import *

def getNumbers():
    nums =[]

    #sentinel loop to get numbers
    xStr =input("Please enter a number (<Enter> to quit): ")
    while xStr != "":
        x = eval(xStr)
        nums.append(x)
        xStr =input("Please enter a number (<Enter> to quit): ")
    return nums

def mean(nums):
    sum = 0.0
    for i in nums:
        sum = sum + i
    return sum/len(nums)

def stdDev(nums, xbar):
    sumDevsq = 0.0
    for i in nums:
        dev = i - xbar
        sumDevsq = sumDevsq + dev**2
    return sqrt(sumDevsq/(len(nums)-1))

def meanStdDev(nums):
    xbar = mean(nums)
    std = stdDev(nums, xbar)
    return xbar, std

def median(nums):
    nums.sort()
    size = len(nums)
    midPos = size //2
    if size % 2 == 0:
       median = (nums[midPos]+nums[midPos-1])/2.0
    else:
       median = nums[midPos]
    return median

def main():
    print("This program computes mean, median, and standard deviation.")
    data = getNumbers()
    xbar = mean(data)
    std = stdDev(data, xbar)
    med = median(data)

    x = 0
    while x != "":
        x = (input('Type "Avg", "Med", "Std", or "AvgStd" (<Enter> to exit)>>>  '))
        if x == 'Avg':
            print(xbar)
        elif x == 'Med': 
            print(med)
        elif x == 'Std':
            print(std)
        elif x == 'AvgStd':
            print(meanStdDev(data))
        elif x == '':
            break
        else:
            print("Please try again.")

if __name__=='__main__': main()
