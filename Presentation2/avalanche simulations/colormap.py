from pylab import *

def colorbar2():
	cdict = {'red': ((0.0, 0.0, 0.0),(0.9, 1.0, 1.01),(1.0, 1.0, 1.0)), 'green': ((0.0, 0.0, 0.0),(0.9, 1.0, 0.0),(1.0, 1.0, 1.0)),'blue': ((0.0, 0.0, 0.0),(0.9, 1.0, 0.0),(1.0, 0.5, 1.0))}
	my_cmap = matplotlib.colors.LinearSegmentedColormap('my_colormap',cdict,256)
	
	rando = rand(10,10)
	print rando
	pcolor(rando,cmap=my_cmap)
	show()

colorbar2()