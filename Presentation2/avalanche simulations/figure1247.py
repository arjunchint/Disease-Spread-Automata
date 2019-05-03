import math
import random
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
from scipy import interpolate as inter

def graph():
	sizearray, durationarray = avalanche(100,100)
	
	#list = dict((i, sizearray.count(i)) for i in sizearray if i >= 1 and sizearray.count(i) > 0)
	countsize = np.histogram(sizearray, 500)
	print "countsize"
	print
	print countsize
	print 
	
	countduration = np.histogram(durationarray, 500)
	
	#list2 = dict((i, durationarray.count(i)) for i in durationarray if i >= 1 and durationarray.count(i) > 0)
	print
	print "countduration"
	print
	print countduration
	
	
	
	x = sizearray
	y = durationarray
	
	print
	print "sizearray"
	print
	print x
	
	print
	print "durationarray"
	print
	print y
	

	logx = np.log(x)
	logy = np.log(y)
	coeffs = np.polyfit(logx,logy,deg=1)
	poly = np.poly1d(coeffs)
	yfit = lambda x: np.exp(poly(np.log(x)))

	plt.subplot(1,2,1)
	line = plt.loglog(x,yfit(x))
	points = plt.loglog(x,y, '.')
	#plt.legend("best fit line: "+str(poly)+"")
	plt.legend(line, ["best fit line = "+str(poly)+""])
	
	plt.plot(np.log(x),np.log(y), '.')
	plt.plot(x,fit_fn(x),'--k')
	plt.xlabel('size = s')
	plt.ylabel('duration')
	plt.yscale('log')
	plt.xscale('log')
	
	plt.title("Avalanche duration versus size")
	
	plt.show()


def avalanche(m,n): 
	lattice = createStartingArray(m,n)
	
	
	S = 0
	D = 0
	size = 0
	sizeArray = []
	avalancheMatrix = createArray(m,n)
	durationArray = []
	while S < 10000:
		size = 0
		D = 0 
		avalancheMatrix = createArray(m,n)
		mCol = int(m*random.random() + 1)
		nRow = int(n*random.random() + 1)
		lattice[mCol,nRow] = lattice[mCol,nRow] + 1
		
		if lattice[mCol,nRow] > 3: 
			lattice[(mCol-1),(nRow)] = lattice[(mCol-1),(nRow)] + 1
			lattice[(mCol),(nRow-1)] = lattice[(mCol),(nRow-1)] + 1
			lattice[(mCol),(nRow+1)] = lattice[(mCol),(nRow+1)] + 1
			lattice[(mCol+1),(nRow)] = lattice[(mCol+1),(nRow)] + 1
			
			lattice[mCol,nRow] = lattice[mCol,nRow] - 4
			
			avalancheMatrix[mCol,nRow] = 1.0
			D = D+1
		
		while checkMatrix(lattice,m,n) is True: 
			
			for i in range(1,(m+1)):
				for j in range(1,(n+1)):
				
					if lattice[i,j] > 3: 
						
						lattice[(i-1),(j)] = lattice[(i-1),(j)] + 1
						lattice[(i),(j-1)] = lattice[(i),(j-1)] + 1
						lattice[(i),(j+1)] = lattice[(i),(j+1)] + 1
						lattice[(i+1),(j)] = lattice[(i+1),(j)] + 1

						lattice[i,j] = lattice[i,j] - 4
						avalancheMatrix[i,j] = 1.0
						
			D = D+1
			
		S = S+1
		size = checkSize(avalancheMatrix,m,n)
		sizeArray = sizeArray + [size]
		durationArray = durationArray + [D]
		
		print size

	return sizeArray, durationArray


def checkSize(array,m,n):

	size = 0
	for i in range(1,(m+1)):
		for j in range(1,(n+1)):
			if array[i,j] > 0:
				size = size + 1
	
	return size

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

graph()