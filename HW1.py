import argparse 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mplpatches
import math

# def argParser():
# 	parser=argparse.ArgumentParser(add_help=True)
# 	parser.add_argument('--outputfile','-o',type=str,help='specify filename of your output file')
# 	print(vars(parser.parse_args()))
# 	return vars(parser.parse_args())

# args = argParser()

# fileName = args['outputfile']

plt.style.use('BME163.mplstyle.txt')

figure_width=3.42
figure_height=2

plt.figure(figsize=(figure_width,figure_height))

panel_width=1/figure_width
panel_height=1/figure_height

panel1=plt.axes([0.1,0.2,panel_width,panel_height])
panel2=plt.axes([0.6,0.2,panel_width,panel_height])



q = list(np.linspace(0,1,25))

j = 0
for i in np.linspace(0,np.pi/2,25):
	panel1.plot(np.sin(i),np.cos(i),color=(q[j],q[j],q[j]),marker='o',markersize=1)
	j += 1




red = (1,0.0)
green = (0,1,0)
blue = (0,0,1)
yellow = (1,1,0)

R = np.linspace(blue[0], yellow[0],100)
G = np.linspace(blue[1],yellow[1],100)
B = np.linspace(blue[2],yellow[2],100)


for index_h in range(0,100,10):
	for index_v in range(0,100,10):
		#use blue and magenta
		rectangle1 = mplpatches.Rectangle([index_h,index_v],10,10,edgecolor='black',facecolor=(R[index_h],G[index_v],B[0]),linewidth=1)
		panel2.add_patch(rectangle1)


panel2.set_xlim(0,100)
panel2.set_ylim(0,100)

panel1.axes.get_xaxis().set_visible(False)
panel1.axes.get_yaxis().set_visible(False)
panel2.axes.get_xaxis().set_visible(False)
panel2.axes.get_yaxis().set_visible(False)




plt.savefig('HW1.png')












