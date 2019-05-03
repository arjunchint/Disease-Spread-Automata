import math
import random
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm

def avalanche(m,n): 
	#initial lattice
	lattice = createStartingArray(m,n)
	
	#plots initial conditions
	plt.subplot(1,2,1)
	plt.title("Initial")
	initial = stripArray(lattice,m,n)
	plt.imshow(initial, cmap=cm.binary, interpolation='nearest')
	plt.axis('off')
	
	
	#sand addition counter
	S = 0
	
	#registers cells involved in the avalanche
	avalancheMatrix = createArray(m,n)
	
	#first while loop, this checks to see if there is an avalanche
	while checkSize(avalancheMatrix,m,n,S) is True:
		
		
		avalancheMatrix = createArray(m,n)
		mCol = int(m*random.random() + 1)
		nRow = int(n*random.random() + 1)
		
		#adds one to a random cell
		lattice[mCol,nRow] = lattice[mCol,nRow] + 1
		
		#if that cell is greater than the critical value - it tumbles
		if lattice[mCol,nRow] > 3: 
			lattice[(mCol-1),(nRow)] = lattice[(mCol-1),(nRow)] + 1
			lattice[(mCol),(nRow-1)] = lattice[(mCol),(nRow-1)] + 1
			lattice[(mCol),(nRow+1)] = lattice[(mCol),(nRow+1)] + 1
			lattice[(mCol+1),(nRow)] = lattice[(mCol+1),(nRow)] + 1
			
			lattice[mCol,nRow] = lattice[mCol,nRow] - 4
			
			avalancheMatrix[mCol,nRow] = 1.0
			
		#second while loop, checks if their is any cells that are critical in the system
		while checkMatrix(lattice,m,n) is True: 
			
			#goes through the entire system, 'tumbling' unstable cells
			for i in range(1,(m+1)):
				for j in range(1,(n+1)):
				
					if lattice[i,j] > 3: 
						lattice[(i-1),(j)] = lattice[(i-1),(j)] + 1
						lattice[(i),(j-1)] = lattice[(i),(j-1)] + 1
						lattice[(i),(j+1)] = lattice[(i),(j+1)] + 1
						lattice[(i+1),(j)] = lattice[(i+1),(j)] + 1

						lattice[i,j] = lattice[i,j] - 4
						
						#keeps track of 'tumbled' cells
						avalancheMatrix[i,j] = 1.0
			
		
		#keeps track of number of sand additions
		S = S+1

		
	#strips the matrices of the outer boundary layer for graphing
	finalAvalanche = stripArray(avalancheMatrix,m,n)
	finalArray = stripArray(lattice,m,n)

	#counts size of the avalanche
	Numb = 0
	for i in range(0,m):
		for j in range(0,n):
			if finalAvalanche[i,j] > 0: 
				Numb = Numb + 1
				finalArray[i,j] = 0.8
	
	
	#plots the last graph (after S iterations)
	plt.subplot(1,2,2)
	plt.title(" Sand Additions = "+str(S)+" Avalanche Size = "+str(Numb)+"")
	plt.imshow(finalArray, cmap=cm.binary, interpolation='nearest')
	plt.axis('off')
			
	plt.show()

#checks the size of the avalanche if it exits
def checkSize(array,m,n,iterations):

	size = 0
	for i in range(1,(m+1)):
		for j in range(1,(n+1)):
			if array[i,j] > 0:
				size = size + 1
	
	if iterations <= 3000: 			
		return True
			
	elif iterations > 3000: 
		if size <= 1000:
			return True
	
		elif size > 1000:
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


avalanche(100,100)