import matplotlib
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

import argparse 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mplpatches
import math
import matplotlib as mpl

plt.style.use('BME163')
mpl.rcParams['xtick.labelsize'] = 5.6
mpl.rcParams['ytick.labelsize'] = 5.6


figure_width=5.0#3.42
figure_height=2.0

plt.figure(figsize=(figure_width,figure_height))

panel_width=1/figure_width
panel_height=1/figure_height

panel1=plt.axes([0.14,0.15,panel_width,panel_height])
panel2=plt.axes([0.076,0.15,0.05,panel_height])
panel3=plt.axes([0.14,0.685,panel_width,0.125])
#panel2=plt.axes([0.6,0.2,panel_width,panel_height])

x_values=[]
y_values=[]
for line in open('BME163_Input_Data_1.txt'):
    a=line.strip().split('\t')
    number1=int(a[1])
    number2=int(a[2])

    x_values.append(number1)
    y_values.append(number2)


x = np.log2([i+1 for i in x_values])
y = np.log2([j+1 for j in y_values])


#for i in range(0,len(x_values)):
panel1.scatter(x,y,s=2,
             color='black',
             marker='o',
             #markeredgecolor='red',
             #markeredgewidth=0,
             #markerfacecolor='black',
             #markersize=1.5,
             linewidth=0,
             #linestyle='--',
             alpha=0.1)

panel1.set_xlim(0,15)
panel1.set_ylim(0,15)
panel1.set_xticks([0,5,10,15])
panel1.set_yticks([])


panel2.set_xticks([20,0])
panel2.set_yticks([0,5,10,15])
#panel2.hist(np.log2(np.asarray(y_values)+1),orientation='horizontal')
panel2.set_ylim(0,15)
panel2.set_xlim(20,0)


panel3.set_ylim(0,20)
#panel3.set_xlim(0,15)
panel3.set_xticks([])

#use np.histogram to produce array
#plot arrays using rectangle function


bins = np.arange(0,30,1)/2
x_histogram, x_bins = np.histogram(x,bins)
x_plot = np.log2([i+1 for i in x_histogram])
for i in range(len(x_plot)):
	temp_rect = mplpatches.Rectangle(((i*panel_width/6),0),(panel_width/6),(x_plot[i]),facecolor='grey',linestyle = '-',linewidth=0.1,edgecolor='black')
	panel3.add_patch(temp_rect)

y_histogram,y_bins = np.histogram(y,bins)
y_plot= np.log2([i+1 for i in y_histogram])
for j in range(len(y_plot)):
	temp_rect = mplpatches.Rectangle((0.075,j*panel_height),y_plot[j],panel_width*2.3125,facecolor='grey',linestyle='-',linewidth=0.1,edgecolor='black')
	panel2.add_patch(temp_rect)







plt.savefig('HW2_week7.pdf',transparent=False)















