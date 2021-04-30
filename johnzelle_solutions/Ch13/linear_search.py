def search(x,nums):
    for i in range(len(nums)):
        if nums[i] == x:
           return i
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
