import math
import random
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm

def avalanche(m,n): 
	lattice = createStartingArray(m,n)
	S = 0
	
	plt.title("Initial")
	initial = stripArray(lattice,m,n)
	plt.imshow(initial, cmap=cm.binary, interpolation='nearest')
	plt.axis('off')
	
	
	D = 0
	size = 0
	sizeArray = []
	#avalancheMatrix = createArray(m,n)
	durationArray = []
	
	while S < 100:
		size = 0
		D = 0 
		
		num = random.random()
		if num < 0.3:
			mCol = 49
			nRow = 49
		
		elif num < 0.5:
			mCol = 50
			nRow = 50
			
		else:
			mCol = 51
			nRow = 51
			
		lattice[mCol,nRow] = lattice[mCol,nRow] + 1
		
		if lattice[mCol,nRow] > 3: 
			lattice[(mCol-1),(nRow)] = lattice[(mCol-1),(nRow)] + 1
			lattice[(mCol),(nRow-1)] = lattice[(mCol),(nRow-1)] + 1
			lattice[(mCol),(nRow+1)] = lattice[(mCol),(nRow+1)] + 1
			lattice[(mCol+1),(nRow)] = lattice[(mCol+1),(nRow)] + 1
			
			lattice[mCol,nRow] = lattice[mCol,nRow] - 4
			
			#avalancheMatrix[mCol,nRow] = 1.0
			D = D+1
	
		R = 0
		while checkMatrix(lattice,m,n) is True: 
			
			for i in range(1,(m+1)):
				for j in range(1,(n+1)):
				
					if lattice[i,j] > 3: 
						
						lattice[(i-1),(j)] = lattice[(i-1),(j)] + 1
						lattice[(i),(j-1)] = lattice[(i),(j-1)] + 1
						lattice[(i),(j+1)] = lattice[(i),(j+1)] + 1
						lattice[(i+1),(j)] = lattice[(i+1),(j)] + 1

						lattice[i,j] = lattice[i,j] - 4
						#avalancheMatrix[i,j] = 1.0
			
		
			finalArray = stripArray(lattice,m,n)
			plt.subplot(1,1,1)
			plt.title(" Sand Additions = "+str(S)+"")
			plt.imshow(finalArray, cmap=cm.binary, interpolation='nearest')
			plt.axis('off')
				
			plt.show()
				
			D = D+1
			
		S = S+1
		
		#size = checkSize(avalancheMatrix,m,n)
		#sizeArray = sizeArray + [size]
		#durationArray = durationArray + [D]
		
		#strips the matrices of the outer boundary layer for graphing
		#finalAvalanche = stripArray(avalancheMatrix,m,n)
		finalArray = stripArray(lattice,m,n)
	
	
		#plots the last graph (after 'time' iterations)
		#plt.subplot(math.ceil((S+1)/6.0),6,S+1)
		#F = str(S)
		#plt.title("After "+F+" Sand Addition(s)")

		plt.subplot(1,2,2)
		plt.title(" Sand Additions = "+str(S)+"")
		plt.imshow(finalArray, cmap=cm.binary, interpolation='nearest')
		plt.axis('off')
		
		
		plt.axis('off')
		
	
			
	plt.show()

def checkSize(array,m,n,iterations):

	size = 0
	for i in range(1,(m+1)):
		for j in range(1,(n+1)):
			if array[i,j] > 0:
				size = size + 1
	
	if iterations <= 1000: 			
		return True
			
	elif iterations > 1000: 
		if size <= 3000:
			return True
	
		elif size > 3000:
			return False
		
def checkMatrix(array,m,n): 
	N = 0
	for i in range(1,(m+1)):
		for j in range(1,(n+1)):
			if array[i,j] > 3:
				N = 1
	
	if N == 0:
		return False
	
	if N == 1: 
		return True

#creates an m x n array of zeros; with a border of 0's around it
def createArray(m,n):
	return np.zeros(((m+2),(n+2)))

#creates a random starting matrix of 0's and 1's; with probability of being alive (example 0.3)
def createStartingArray(m,n):
	arr = createArray(m,n)
	
	for i in range(1,(m+1)):
		for j in range(1,(n+1)):
			num = random.random()
			if num < 0.5:
				arr[i,j] = 3
			else:
				arr[i,j] = 2

	return arr
	
#creates a striped array of only the inner nxm matrix and inverts it
def stripArray(arr,m,n):
	strippedArray = createArray((m-2),(n-2))
	
	for i in range(1,(m+1)):
		for j in range(1,(n+1)):
			strippedArray[(i-1),(j-1)] = arr[i,j] / 3.0

	return strippedArray

def noAvalanche(array,m,n):
	
	number = 0
	for i in range(1,(m+1)):
		for j in range(1,(n+1)):
			if array[i,j] == 1:
				nW = array[(i-1),(j-1)]
				north = array[(i-1),(j)]
				nE = array[(i-1),(j+1)]
				west = array[(i),(j-1)]
				east = array[(i),(j+1)]
				sW = array[(i+1),(j-1)]
				south = array[(i+1),(j)]
				sE = array[(i+1),(j+1)]
				
				sum = (nW + north + nE + west + east + sW + south + sE)
				print "sum =" + str(sum)
				
				if sum > 20:
					print "sum =" + str(sum)
					number = number + 1
	
	if number > 15: 
		return False
		
	else:
		return True


avalanche(100,100)