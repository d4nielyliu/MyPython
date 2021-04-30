def search(x,nums):
    low = 0
    high = len(nums)-1
    while high >= low:
        mid = (low+high)//2
        item = nums[mid]
        if x == item:
            return mid
        elif x < item:
            high = mid - 1
        else:
            low = mid + 1
    return -1

def main():
    nums = []
    x = eval(input("Enter a number you would like to search >> "))
    xStr = input("Enter a numer (<Enter> to quit) >> ")
    while xStr != "":
        a = eval(xStr)
        nums.append(a)
        xStr = input("Enter a numer (<Enter> to quit) >> ")
    print(search(x,nums))

if __name__ == '__main__': main()
