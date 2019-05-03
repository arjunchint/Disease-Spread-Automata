#creates a striped array of only the inner nxm matrix and inverts it
def stripArrayAndInvert(arr,m,n):
	strippedArray = createArray((m-2),(n-2))
	
	for i in range(1,(m+1)):
		for j in range(1,(n+1)):
			strippedArray[(i-1),(j-1)] = arr[i,j]
	
	invertAndStrip = invertValues(strippedArray,m,n)

	return invertAndStrip
	
#inverts the values of the maxtrix
def invertValues(matrix,m,n):
	invertArr = createArray((m-2),(n-2))
	for i in range(0,(m)):
		for j in range(0,(n)):
			invertArr[i,j] = (1 - matrix[i,j])
	
	
	return invertArr
	
	
gameOfLife(100,100,250,0.3)