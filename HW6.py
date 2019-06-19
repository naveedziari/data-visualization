import argparse 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mplpatches
import math

plt.style.use('BME163')

matplotlib.rcParams['pdf.fonttype'] = 42


figure_width=5
figure_height=3

plt.figure(figsize=(figure_width,figure_height))

panel_width=1/figure_width
panel_height=1/figure_height


panel1=plt.axes([0.5/figure_width,0.1,0.75/figure_width,2.5/figure_height])




data = []
skip = True
for line in open('BME163_Input_Data_4.txt'):
	if skip:
		skip = False
		continue
	x = line.strip().split('\t')
	temp_array = [int(i) for i in x[4:12]]
	temp_array = [(j-min(temp_array))/(max(temp_array)-min(temp_array))*100 for j in temp_array]
	temp_array.append(float(x[13]))
	data.append(temp_array)

data = sorted(data,key=lambda x:x[-1], reverse=True)


panel1.set_xlim([0,8])
panel1.set_xticks([i+0.5 for i in range(8)])
panel1.set_xticklabels(['0','','6','','12','','18'])
panel1.set_ylim([0,len(data)])
panel1.set_yticks([i for i in range(0,1201,200)])
panel1.set_ylabel('Number of genes')
panel1.set_xlabel('CT')

Yellow=(255,220,0)
White=(255,255,255)
Blue=(56,66,156)
R=np.linspace(Yellow[0]/255,Blue[0]/255,101)
G=np.linspace(Yellow[1]/255,Blue[1]/255,101)
B=np.linspace(Yellow[2]/255,Blue[2]/255,101)

y=0
for row in data:
	x=0
	for position in row[:-1]:
		color=(R[int(position)],G[int(position)],B[int(position)])
		rectangle=mplpatches.Rectangle([x,y],1,1,facecolor=color,linewidth=0)
		panel1.add_patch(rectangle)
		x+=1
	y+=1


panel2=plt.axes([1.75/figure_width,0.1,2.5/figure_width,2.5/figure_height])

panel2.set_ylim([-4,4])
panel2.set_xlim([-4,4])


panel2.text(0,0,'CT', verticalalignment='center',horizontalalignment='center',fontsize=6)
panel2.text(-2,0,'100', verticalalignment='center',horizontalalignment='right',fontsize=6)
panel2.text(-3,0,'200', verticalalignment='center',horizontalalignment='right',fontsize=6)
panel2.text(-4,0,'300', verticalalignment='center',horizontalalignment='right',fontsize=6)
panel2.text(0,0.5,'0', verticalalignment='center',horizontalalignment='center',fontsize=6)
panel2.text(0,-0.5,'12', verticalalignment='center',horizontalalignment='center',fontsize=6)
panel2.text(0.45,0.25,'4', verticalalignment='center',horizontalalignment='center',fontsize=6)
panel2.text(0.45,-0.25,'8', verticalalignment='center',horizontalalignment='center',fontsize=6)
panel2.text(-0.45,0.25,'20', verticalalignment='center',horizontalalignment='center',fontsize=6)
panel2.text(-0.45,-0.25,'16', verticalalignment='center',horizontalalignment='center',fontsize=6)



for radius in np.arange(0.82,0.98,0.01):
    x_list=[]
    y_list=[]
    for rad in np.linspace(-np.pi/2,np.pi/2,1000):
        x=np.cos(rad)*radius
        y=np.sin(rad)*radius
        x_list.append(-x)
        y_list.append(y)

    panel2.plot(x_list,y_list, markersize=0.05, marker='o', markeredgewidth=0,color='black')


#generate histogram
bins_var = list(range(0,26,2))
phase_vals = [i[-1] for i in data]
phase_hist = np.histogram(phase_vals,bins = np.arange(0,26,2))
temp_array = list(phase_hist[0])
temp_array = list(reversed(temp_array))

for i in range(len(phase_hist[0])):
    x_list = []
    y_list = []
    boundaries = np.arange(phase_hist[1][i],(phase_hist[1][i]+2),0.01)
    line_boundaries = np.arange(phase_hist[1][i],phase_hist[1][i]+2.1,2)
    radius = (temp_array[i])/100 + 1
    for k in line_boundaries:
        scaled_point = (k/24)*(np.pi*2)
        x_val = np.cos(scaled_point+(np.pi/2))*radius
        y_val = np.sin(scaled_point+(np.pi/2))*radius 
        panel2.plot([x_val/radius,x_val],[y_val/radius,y_val], markersize = 0,marker = 'o',markeredgewidth=0,color = 'black',linewidth=0.8)
    for point in boundaries:
        scaled_point = (point/24)*(np.pi*2)
        x_val = np.cos(scaled_point+(np.pi/2))*radius
        y_val = np.sin(scaled_point+(np.pi/2))*radius
        x_list.append(x_val)
        y_list.append(y_val)
        panel2.plot([x_val/radius,x_val],[y_val/radius,y_val], markersize = 0,marker = 'o',markeredgewidth=0,color = 'grey',linewidth=0.3)

    panel2.plot(x_list,y_list, markersize=0.05, marker='o', markeredgewidth=0,color='black',linewidth = 0.5)

for radius in np.arange(2,5,1):
    x_list=[]
    y_list=[]
    for rad in np.linspace(-np.pi,np.pi,1000):
        x=np.cos(rad)*radius
        y=np.sin(rad)*radius
        x_list.append(x)
        y_list.append(y)

    line1, = panel2.plot(x_list,y_list, markersize=0, marker='o', markeredgewidth=0,color='black',linewidth=0.3,linestyle='--')
    line1.set_dashes([6.5,7,13,7])

for radius in [0.8,1]:
    x_list=[]
    y_list=[]
    for rad in np.linspace(-np.pi,np.pi,1000):
        x=np.cos(rad)*radius
        y=np.sin(rad)*radius
        x_list.append(x)
        y_list.append(y)


    panel2.plot(x_list,y_list, markersize=0, marker='o', markeredgewidth=0,color='black',linewidth=0.5)


panel2.set_axis_off()



plt.savefig('Ziari_Naveed_Assignment_Week6.png')






