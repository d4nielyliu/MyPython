def recPower(a,n):
    if n == 0:
       return 1
    else:
       factor = recPower(a, n//2)
       if n%2 == 0:
            return factor**2
       else:
            return factor**2*2
