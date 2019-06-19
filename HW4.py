import matplotlib
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

import argparse 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mplpatches
import math
import random

plt.style.use('BME163.mplstyle.txt')


figure_width=7.0
figure_height=3.0

plt.figure(figsize=(figure_width,figure_height))


#load data
count = 0
data = {str(i+1):[] for i in range(10)}
data['>10'] = []
for line in open('BME163_Input_Data_3.txt'):
	a=line.strip().split('\t')
	temp_string = str(a[0])
	temp_val = float(a[1])
	subread = temp_string.split('_')[3]
	if int(subread) > 10: data['>10'].append(temp_val)
	else: data[subread].append(temp_val)


panel_width = 5.0/7
panel_height = 2.0/3
plt.axes([1.0/10,1.0/5,panel_width,panel_height])
plt.ylim(75,100,5)
plt.xlim(0,22)
plt.xlabel('Subread coverage')
plt.ylabel('Identity (%)')
plt.xticks([i+1 for i in range(0,21,2)],list(data.keys()))
line1, = plt.plot(range(23),[95]*23,linestyle='--',color='black',linewidth=0.5)
line1.set_dashes([4,8,8,8])


def swarmplot(y_vals,panel_height,panel_width,counter):
	cutoff = 0.008
	plotted = []
	i=0
	overlap = True
	for y_val in y_vals:
		x_val = 0
		for coordinate in plotted:
			if np.sqrt(((coordinate[0]-x_val)/22*panel_width)**2+((coordinate[1]-y_val)/25*panel_height)**2) < cutoff:
				overlap = True
			else: overlap = False
			if overlap == True:
				if i % 2 == 0: x_val += cutoff
				else: x_val -= cutoff
		i += 1
		plotted.append((x_val,y_val))

	return [i[0] for i in plotted]



counter = 1
for k,v in data.items():
	subsample = random.sample(v,1000)
	
	#if k == '2':
	x_coord = swarmplot(subsample,panel_width,panel_height,counter)
	plt.scatter([k+counter for k in x_coord],subsample,s=2,color='black',marker='.',linewidth=0)#facecolors='black',edgecolors='black')
	plt.plot([counter-0.8,counter,counter+0.8],[np.median(v)]*3,color='red',linewidth=0.8)
	counter += 2


panel1 = plt.axes([0.1,0.2+(panel_height*0.8)+0.055,0.08,0.08])
panel1.set_xlim([0,1])
panel1.set_ylim([0,1])
panel1.set_xticks([])
panel1.set_yticks([])
panel1.plot([0.35,0.65],[0.8,0.8],linewidth=1,color='red',markersize=0)
panel1.text(0.5,0.25,'Median',verticalalignment='center',horizontalalignment='center',fontsize=8)




plt.savefig('HW4_week7.pdf',transparent=True)












