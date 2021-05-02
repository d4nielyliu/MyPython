def selectionSort(array):
    # Write your code here.
    n = len(array)
	
    for bottom in range(n-1):
        mp = bottom
        for i in range(bottom+1,n):
            if array[i] < array[mp]:
                mp = i
  
        array[bottom], array[mp] = array[mp], array[bottom]

    print(array)
