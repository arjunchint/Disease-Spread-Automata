import math
import random
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
from scipy import interpolate as inter



def graph():
	
	y= ([6094,  493,  541,  180,  272,   94,   97,  140,   59,  121,   54,
        100,   46,   34,   86,   40,   63,   22,   56,   19,   28,   59,
         16,   44,   26,   41,   15,   19,   37,   16,   33,   15,   28,
         17,   15,   27,    9,   24,   17,   29,    8,   15,   24,    9,
         23,    6,   31,   10,   11,   12,   15,    9,    7,   17,   14,
         11,   21,    6,   18,    9,   23,    6,    6,    8,    6,   11,
          6,   10,    6,    6,   11,    7,    8,    5,   14,    4,    2,
         13,    7,    9,    3,   10,    2,    6,    9,    8,    6,    8,
         11,    5,    5,    7,    6,   10,    2,    8,    4,    3,    9,
          1,   13,    3,    3,    3,    2,    9,    3,    9,    2,    8,
          5,    4,    6,    4,    8,    2,   13,    2,    3,    5,    7,
          7,    3,    4,    4,    1,    9,    2,    5,    1,    5,    4,
          2,    2,    2,    3,    1,    2,    2,    3,    5,    2,    4,
          1,    5,    3,    3,    4,    1,    3,    1,    2,    1,    2,
          3,    1,    4,    3,    1,                1,   
          3,    1,    2,    2,    1,    6,    1,    1,    1,    1,    3,
             2,          1,    1,    4,       2,       2,
          1,                   2,    2,         
          3,       1,                2,          1,
          1,    1,    1,    3,    2,    1,          2,    1,    1,
          1,    1,                1,    1,         
                   1,                   1,   
          1,       1,                        
                      1,             1,      
          1,          1,    1,             1,      
                         1,               
                   1,                     
                               1,         
             1,                           
                                       
          1,                              
                                       
                                       
                                       
                                       
                                       
                                       
                                  1,      
                                       
                                       
                                       
                                       
                                       
                                       
                      1,                  
                      1])
  	
  	x =  [1, 1.428, 2.856, 4.284, 5.712, 7.14, 8.568, 9.996, 11.424, 12.852, 14.28, 15.708, 17.136, 18.564, 19.992, 21.42, 22.848, 24.276, 25.704, 27.132, 28.56, 29.988, 31.416, 32.844, 34.272, 35.7, 37.128, 38.556, 39.984, 41.412, 42.84, 44.268, 45.696, 47.124, 48.552, 49.98, 51.408, 52.836, 54.264, 55.692, 57.12, 58.548, 59.976, 61.404, 62.832, 64.26, 65.688, 67.116, 68.544, 69.972, 71.4, 72.828, 74.256, 75.684, 77.112, 78.54, 79.968, 81.396, 82.824, 84.252, 85.68, 87.108, 88.536, 89.964, 91.392, 92.82, 94.248, 95.676, 97.104, 98.532, 99.96, 101.388, 102.816, 104.244, 105.672, 107.1, 108.528, 109.956, 111.384, 112.812, 114.24, 115.668, 117.096, 118.524, 119.952, 121.38, 122.808, 124.236, 125.664, 127.092, 128.52, 129.948, 131.376, 132.804, 134.232, 135.66, 137.088, 138.516, 139.944, 141.372, 142.8, 144.228, 145.656, 147.084, 148.512, 149.94, 151.368, 152.796, 154.224, 155.652, 157.08, 158.508, 159.936, 161.364, 162.792, 164.22, 165.648, 167.076, 168.504, 169.932, 171.36, 172.788, 174.216, 175.644, 177.072, 178.5, 179.928, 181.356, 182.784, 184.212, 185.64, 187.068, 188.496, 189.924, 191.352, 192.78, 194.208, 195.636, 197.064, 198.492, 199.92, 201.348, 202.776, 204.204, 205.632, 207.06, 208.488, 209.916, 211.344, 212.772, 214.2, 215.628, 217.056, 218.484, 219.912, 221.34, 222.768, 224.196, 225.624, 232.764, 235.62, 237.048, 238.476, 239.904, 241.332, 242.76, 244.188, 245.616, 247.044, 248.472, 249.9, 252.756, 257.04, 258.468, 259.896, 262.752, 265.608, 267.036, 275.604, 277.032, 282.744, 285.6, 292.74, 297.024, 298.452, 299.88, 301.308, 302.736, 304.164, 305.592, 309.876, 311.304, 312.732, 314.16, 315.588, 322.728, 324.156, 334.152, 342.72, 345.576, 348.432, 366.996, 372.708, 376.992, 381.276, 382.704, 388.416, 399.84, 412.692, 434.112, 441.252, 471.24, 592.62, 696.864, 712.572]


  #list = dict((i, x.count(i)) for i in array if i >= 1 and x.count(i))
	
	#print x 
	#print y
	
	#for i in range(0,500):
		#if y[i] == 0:
		#	x[i] = 0.1
	
	#print x
	#print y
	
	#x = list.keys()
	#y = list.values()
	
	
	#x = bins
	#y = values
	
	#fit = np.polyfit(np.log(x),np.log(y),1)
	#fit_fn = np.poly1d(fit)
	
	logx = np.log(x)
	logy = np.log(y)
	coeffs = np.polyfit(logx,logy,deg=1)
	poly = np.poly1d(coeffs)
	yfit = lambda x: np.exp(poly(np.log(x)))

	#plt.subplot(1,2,1)
	line = plt.loglog(x,yfit(x))
	points = plt.loglog(x,y, '.k')
	#plt.legend("best fit line: "+str(poly)+"")
	plt.legend(line, ["least-squares fit line: "+str(poly)+""])
	#legend([points], ["scatter plot"])
	
	#print coeffs
	#print poly
	
	#tau = fit()
	#k = exp(fit()
	
	plt.title("Distribution of Avalanche Duration ")
	plt.xlabel('duration')
	plt.ylabel('number of avalanches')
	#plt.plot(x, fit_fn(x),'--k')
	
	#plt.subplot(1,2,2)
	
	
	#plt.plot(x,fit_fn(x), '--k')
	#plt.plot(x,fit_fn(x),'--k')
	#plt.xlabel('size = s')
	#plt.ylabel('number of avalanches')
	#plt.xscale('log')
	#plt.yscale('log')
	
	#plt.subplot(1,2,2)
	#plt.loglog(x,y, '.')
	#plt.title("Distribution of avalanche sizes")
	#plt.xlabel('size = s')
	#plt.ylabel('number of avalanches')
	#n = plt.hist(array)
	#print n
	
	
	
	
	plt.show()

graph()
         
