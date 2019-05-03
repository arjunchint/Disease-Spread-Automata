import math
import random
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.animation as animation


#m rows, n columns, initial probability of a cell being alive, time steps allowed
def gameOfLife(m,n,prob):

	#creates empty figure (100x100)
	initial = createArray(m,n)
	fig = plt.imshow(initial, cmap = plt.gray(), interpolation = 'nearest')
	sub = fig.add_subplot(111,xlim=(0, 100), ylim=(0, 100))


	ani = animation.FuncAnimation(fig, animate, frames=300, blit=True, init_func = int)
	plt.show()
	
#initialize animation
def init():
	global m,n,prob
	
	old = createRandomArray(m,n,prob)
	new = createArray(m,n)
	
	return old, new

#creates an m x n array of zeros; with a border of 0's around it
def createArray(m,n):
	return np.zeros(((m+2),(n+2)), dtype=np.int)

#creates a random starting matrix of 0's and 1's; with probability of being alive (example 0.3)
def createRandomArray(m,n,prob):
	arr = createArray(m,n)
	
	for i in range(1,(m+1)):
		for j in range(1,(n+1)):
			num = random.random()
			if num > (1-prob):
				cell = 1
			else:
				cell = 0
			arr[i,j] = cell
	
	return arr

#creates a striped array of only the inner nxm matrix
def stripArray(arr,m,n):
	strippedArray = createArray((m-2),(n-2))
	
	for i in range(1,(m+1)):
		for j in range(1,(n+1)):
			x = arr[i,j]
			strippedArray[(i-1),(j-1)] = x
			
	return strippedArray
	
#plots an array of size mxn 
def plotArray(f,m,n):
	for i in range(0,m):
		for j in range(0,n):
			if f[i,j] == 1:
				plt.plot(i,j,'ks')
			if f[i,j] == 0:
				plot.plot(i,j,'ws')
					
def animate(t):
	global m,n,old,new
	
	for i in range(1,(m+1)):
		sum = 0
		for j in range(1,(n+1)):
			#check cells around old "board game" -- one time step before
			
			nW = old[i-1,j-1]
			north = old[(i-1),(j)]
			nE = old[(i-1),(j+1)]
			west = old[(i-1),(j)]
			east = old[(i),(j+1)]
			sW = old[(i+1),(j-1)]
			south = old[(i+1),(j)]
			sE = old[(i-1),(j+1)]
					
			sum = (nW+north+nE+west+east+sW+south+sE)
					
			if sum == 3:
				new[i,j] = old[i,j]
					
			elif sum == 2: 
				new[i,j] = 1
					
			elif sum > 3 or sum < 2:
				new[i,j] = 0

	
	old = new
	
	return old, new
	

gameOfLife(10,10,0.3)