#imports appropriate packages
import math
import random
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm

#m rows, n columns, initial probability of a cell being alive, time steps allowed
def gameOfLife(m,n,time,prob):

  #creates original; initial matrix of each cell alive with a certain probability
  previous = createRandomArray(m,n,prob)

  #plots the original array
  plt.subplot(1,2,1)
  plt.title("Inital")
  inital = stripArray(previous,m,n)
  plt.imshow(inital, cmap=cm.binary, interpolation='nearest')
  plt.axis('off')

  #creates a 'gray' matrix
  gray = createArray(m,n)

  #time loop, to do a given number of iterations
  for T in range(0, time):

    #creates a new 'next' matrix each time iteration
    next = createArray(m,n)
    F = 0

    #goes through each cell of the matrix
    for i in range(1,(m+1)):
      for j in range(1,(n+1)):

        #check cells around old "board game" -- one time step before
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

	#if the cell is alive
	if previous[i,j] == 1:

	  #has two neighbors alive; stays alive
	  if sum == 2:
	    next[i,j] = 1
	    gray[i,j] = 1

	  #has three neighbors alive; stays alive
	  elif sum == 3:
	    next[i,j] = 1
	    gray[i,j] = 1

	  #has either greater than three neighbors alive
	  #or less than two; dies
	  else:
	    next[i,j] = 0
	    gray[i,j] = 1

	#if the cell is dead
	if previous[i,j] == 0:

	  #has three neighbors alive; becomes alive
	  if sum == 3:
	    next[i,j] = 1
	    gray[i,j] = 1

          #has any number of neighbors; stays dead
	  #if a cell starts dead and never becomes alive
          #the cell remains white
	  else:
	    next[i,j] = 0

    #sets the previous matrix equal to the calculated new values
    previous = next

  #strips the matrices of the outer boundary layer for graphing
  finalArray = stripArray(next,m,n)
  finalGray = stripArray(gray,m,n)

  #sets the graph so that a dead cell if alive in any of the iterations, it will appear gray
  for i in range(0,m):
    for j in range(0,n):

      #if the gray matrix shows the cell to have been alive at one point
      #and the final array that cell is dead then the cell will be gray

      if finalGray[i,j] == 1 and finalArray[i,j] == 0:
        finalArray[i,j] = 0.35

  #plots the last graph (after 'time' iterations)
  plt.subplot(1,2,2)
  plt.title("After "+str(time)+" Iteration(s)")
  plt.imshow(finalArray, cmap=cm.binary, interpolation='nearest')
  plt.axis('off')

  plt.show()


#creates an m x n array of zeros; with a border of 0's around it
def createArray(m,n):
  return np.zeros(((m+2),(n+2)))

# creates a random starting matrix of 0's and 1's; with probability of being alive (example 0.3)
def createRandomArray(m,n,prob):

    arr = createArray(m,n)
    for i in range(1,(m+1)):
        for j in range(1,(n+1)):
            num = random.random()
            if (num < prob):
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

#runs the program 100x100 table, 350 iterations, at 0.3 initial probability
gameOfLife(100,100,350,0.3)
