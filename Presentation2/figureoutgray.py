import math
import random
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm

def gray():
	
	array = createRandomArray(m,n,prob)
	
	





def createArray(m,n):
	return np.zeros((m+2),(n+2))

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
