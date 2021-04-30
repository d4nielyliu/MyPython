def getNthFib(n):
    # Write your code here.
    if n < 3:
       return 1
    else:
       return getNthFib(n-1)+getNthFib(n-2)
