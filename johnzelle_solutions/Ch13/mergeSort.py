def mergeSort(array):
    # Write your code here.
	if len(array) == 1:
		return array
	m = len(array)//2
	L = array[:m]
	R = array[m:]
	return merge(mergeSort(L),mergeSort(R))


def merge(array1, array2):
	n1, n2 = len(array1), len(array2)
	array = [None]*(n1+n2)
	i1, i2, i = 0, 0, 0
	while i1 < n1 and i2 < n2:
		if array1[i1] <= array2[i2]:
			array[i] = array1[i1]
			i1 = i1 + 1
		else:
			array[i] = array2[i2]
			i2 = i2 + 1
		i = i + 1
	
	while i1 < n1:
		array[i] = array1[i1]
		i1 = i1 + 1
		i = i + 1
		
		
	while i2 < n2:
		array[i] = array2[i2]
		i2 = i2 +1
		i = i + 1
	return array
