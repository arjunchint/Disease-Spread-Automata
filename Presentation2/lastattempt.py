import math
import random
import numpy as np
from matplotlib import pyplot as plt


def iterate(m,n,time,start):
	old = start
	array = createArray(m,n)
	new = array

#m rows, n columns, initial probability of a cell being alive, time steps allowed
def gameOfLife(m,n,time):
	array = createArray(m,n)
	plt.subplot(1,2,1)
	plt.title("Inital")
	#plt.axis('off')
	old = array
	old[2,3] = 1
	old[3,4] = 1
	
	plt.imshow(old, cmap='gray', interpolation='nearest')
	
	array2 = createArray(m,n)
	new = array2
	
	for i in range(1,(m+1)):
		for j in range(1,(n+1)):
				
			#check cells around old "board game" -- one time step before
			nW = old[(i-1),(j-1)]
			print nW
			north = old[(i-1),(j)]
			print north
			nE = old[(i-1),(j+1)]
			print nE
			west = old[(i),(j-1)]
			print west
			east = old[(i),(j+1)]
			print east
			sW = old[(i+1),(j-1)]
			print sW
			south = old[(i+1),(j)]
			print south
			sE = old[(i+1),(j+1)]
			print sE
				
			sum = (nW + north + nE + west + east + sW + south + sE)
			print sum 
			
			if old[i,j] == 1:
				if sum == 2:
					new[i,j] = 1
					print "alive alive 2"
					print i, j
				elif sum == 3:
					new[i,j] = 1
					print "alive alive 3"
					print i,j
		
				else:
					new[i,j] = 0		
					print "alive dead else" 
					print i,j
							
			if old[i,j] == 0:
				if sum == 3:				
					new[i,j] = 1
					print "dead alive 3"
					print i,j
					
				else: 
					new[i,j] = 0
					print "dead dead else" 
					print i,j

			
	finalArray = stripArray(new,m,n)
	plt.subplot(1,2,2)
	plt.title("After 1 Iteration")
	plt.imshow(new, cmap='gray', interpolation='nearest')
	#plt.axis('off')
		

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

#creates a striped array of only the inner nxm matrix
def stripArray(arr,m,n):
	strippedArray = createArray((m-2),(n-2))
	
	for i in range(1,(m+1)):
		for j in range(1,(n+1)):
			strippedArray[(i-1),(j-1)] = arr[i,j]


	return strippedArray
	

#plots an array of size mxn 
def plotArray(f,m,n):
	for i in range(0,m):
		for j in range(0,n):
			if f[i,j] == 1:
				plt.plot(i,j,'ks')
			if f[i,j] == 0:
				plt.plot(i,j,'ws')
	
	return plt.show()
	
gameOfLife(8,8,5)


