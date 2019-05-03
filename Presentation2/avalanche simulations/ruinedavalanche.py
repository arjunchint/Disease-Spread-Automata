import math
import random
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm

def avalanche(m,n): 
	
	previous = createStartingArray(m,n)
	
	plt.subplot(1,2,1)
	plt.title("Inital")
	initial = stripArray(previous,m,n)
	plt.imshow(initial, cmap=cm.binary, interpolation='nearest')
	plt.axis('off')
	
	next = createArray(m,n)
	next = previous
	S = 0
	avalancheMatrix = createArray(m,n)
	
	while checkSize(previous,m,n,S) is True:
		avalancheMatrix = createArray(m,n)
		mCol = int(m*random.random() + 1)
		nRow = int(n*random.random() + 1)
		#print "mCol =" + str(mCol)
		#print "nRow =" + str(nRow)
		next[mCol,nRow] = previous[mCol,nRow] + 1
		
		if next[mCol,nRow] > 3: 
			next[(mCol-1),(nRow)] = previous[(mCol-1),(nRow)] + 1
			next[(mCol),(nRow-1)] = previous[(mCol),(nRow-1)] + 1
			next[(mCol),(nRow+1)] = previous[(mCol),(nRow+1)] + 1
			next[(mCol+1),(nRow)] = previous[(mCol+1),(nRow)] + 1
			
			next[mCol,nRow] = previous[mCol,nRow] - 3
			
			avalancheMatrix[mCol,nRow] = 1.0
			#print next
			
		previous = next
		
		while checkMatrix(previous,m,n) is True: 
			for i in range(1,(m+1)):
				for j in range(1,(n+1)):
				
					if previous[i,j] > 3: 
						#check cells around old "board game" -- one time step before
						next[(i-1),(j)] = previous[(i-1),(j)] + 1
						next[(i),(j-1)] = previous[(i),(j-1)] + 1
						next[(i),(j+1)] = previous[(i),(j+1)] + 1
						next[(i+1),(j)] = previous[(i+1),(j)] + 1

						next[i,j] = previous[i,j] - 4
						avalancheMatrix[i,j] = 1.0
					
					
			previous = next
							
			#sets the previous matrix equal to the calculated new values  			
			#previous = next
			#print next
			#print previous
			
		S = S+1
		print S

		
	#strips the matrices of the outer boundary layer for graphing
	finalAvalanche = stripArray(avalancheMatrix,m,n)
	finalArray = stripArray(previous,m,n)

	#sets the graph so that a dead cell if alive in any of the iterations, it will appear gray
	avalanchesize = 0
	for i in range(0,m):
		for j in range(0,n):
			if finalAvalanche[i,j] > 0:
				avalanchesize = avalanchesize + 1
				finalArray[i,j] = 0.8
	
	
	
	#plots the last graph (after 'time' iterations)
	plt.subplot(1,2,2)
	plt.title(" Sand Additions = "+str(S)+" Avalanche Size = "+str(avalanchesize)+"")
	plt.imshow(finalArray, cmap=cm.binary, interpolation='nearest')
	plt.axis('off')
			
	#plt.subplot(1,3,3)
	#plt.title("After "+str(S)+" Sand Additions")
	#plt.imshow(finalAvalanche, cmap=cm.binary, interpolation='nearest')
	#plt.axis('off')
			
			
			
	plt.show()


def checkSize(array,m,n,iterations):
	if iterations > 100:
		
		size = 0
		for i in range(1,(m+1)):
			for j in range(1,(n+1)):
				if array[i,j] == 1.0/3.0:
					size = size + 1
				
		if size <= 20:
			return True
	
		elif size > 20:
			return False
	
	else:
		return True
		
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
				arr[i,j] = 3.0
			else:
				arr[i,j] = 2.0
	
	return arr
	
#creates a striped array of only the inner nxm matrix and inverts it
def stripArray(arr,m,n):
	strippedArray = createArray((m-2),(n-2))
	
	for i in range(1,m+1):
		for j in range(1,n+1):
			strippedArray[(i-1),(j-1)] = (arr[i,j] / 3.0)

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


avalanche(10,10)