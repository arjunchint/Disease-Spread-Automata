import math
import random
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm

#m rows, n columns, initial probability of a cell being alive, time steps allowed
def gameOfLife(m,n,time):
	previous = createArray(m,n)
	#previous[2,3] = 1
	#previous[3,4] = 1
	#previous[4,2] = 1
	#previous[4,3] = 1
	#previous[4,4] = 1
	
	#previous[3,3] = 1
	#previous[3,4] = 1
	#previous[4,4] = 1
	#previous[4,5] = 1
    previous[50,50]
	
	plt.subplot(math.ceil((time+1)/6.0),6,1)
	plt.title("Inital")

	inital = stripArray(previous,m,n)
	plt.imshow(inital, cmap=cm.binary, interpolation='nearest')
	plt.axis('off')
	
	for T in range(0, time):
		next = createArray(m,n)
		F = 0
		for i in range(1,(m+1)):
			for j in range(1,(n+1)):
				
				nW = previous[(i-1),(j-1)]
				north = previous[(i-1),(j)]
				nE = previous[(i-1),(j+1)]
				west = previous[(i),(j-1)]
				east = previous[(i),(j+1)]
				sW = previous[(i+1),(j-1)]
				south = previous[(i+1),(j)]
				sE = previous[(i+1),(j+1)]
				
				#sums each 'N,W,E,S' value
				sum = (nW + north + nE + west + east + sW + south + sE)
			
			
				if previous[i,j] == 1:
					next[i,j] =1 
				if previous[i,j] == 0:
					if sum == 1:				
						next[i,j] = 1
					
					#else: 
						#next[i,j] = 0

		finalArray = stripArray(next,m,n)
		
		plt.subplot(math.ceil((time+1)/6.0),6,T+2)
		F = str(T+1)
		plt.title("After "+F+" Iteration(s)")
		plt.imshow(finalArray, cmap=cm.binary, interpolation='nearest')
		previous = next
		plt.axis('off')
			
	plt.show()


#creates an m x n array of zeros; with a border of 0's around it
def createArray(m,n):
	return np.zeros(((m+2),(n+2)), dtype=np.int)

#creates a random starting matrix of 0's and 1's; with probability of being alive (example 0.3)
def createRandomArray(m,n,prob):
	arr = createArray(m,n)
	
	for i in range(1,(m+1)):
		for j in range(1,(n+1)):
			num = random.random()
			if num < prob:
				arr[i,j] = 1
			else:
				arr[i,j] = 0
	
	return arr

#creates a striped array of only the inner nxm matrix and inverts it
def stripArray(arr,m,n):
	strippedArray = createArray((m-2),(n-2))
	
	for i in range(1,(m+1)):
		for j in range(1,(n+1)):
			strippedArray[(i-1),(j-1)] = arr[i,j]


	return strippedArray
	
#inverts the values of the maxtrix
def invertValues(matrix,m,n):
	invertArr = createArray((m-2),(n-2))
	for i in range(0,(m)):
		for j in range(0,(n)):
			invertArr[i,j] = (1 - matrix[i,j])
	
	
	return invertArr
	
	
#plots an array of size mxn 
def plotArray(f,m,n):
	for i in range(0,m):
		for j in range(0,n):
			if f[i,j] == 1:
				plt.plot(i,j,'ks')
			if f[i,j] == 0:
				plt.plot(i,j,'ws')
	
	return plt.show()
	
gameOfLife(100,100,5)


