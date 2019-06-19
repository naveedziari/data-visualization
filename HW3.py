import matplotlib
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42


import argparse 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mplpatches
import math

plt.style.use('BME163.mplstyle.txt')


figure_width=3.0
figure_height=3.0

plt.figure(figsize=(figure_width,figure_height))

panel_width=2/figure_width
panel_height=2/figure_height

plt.axes([figure_width/18,figure_height/18,panel_width,panel_height])

plt.ylim(-0.05,60)
plt.xlim(-12,12)
plt.xlabel('$\mathregular{log_{2}}$(fold change)')
plt.ylabel('-$\mathregular{log_{10}}$(p-value)')


genes = []
fold_changes = []
p_values = []
for line in open('BME163_Input_Data_2.txt'):
	a=line.strip().split('\t')
	if 'NA' in a: continue
	genes.append(str(a[0]))
	fold_changes.append(float(a[1]))
	p_values.append(-np.log10(float(a[2])))

plt.scatter(fold_changes,p_values,s=2,
             color='black',
             marker='o',
             #markeredgecolor='red',
             #markeredgewidth=0,
             #markerfacecolor='black',
             #markersize=1.5,
             linewidth=0,
             #linestyle='--',
             alpha=1)

print(len(fold_changes))

for i in range(len(fold_changes)):
	if p_values[i] > 8.0:
		if 2**np.abs(fold_changes[i]) > 10:
			plt.scatter(fold_changes[i],p_values[i],s=2,color='red',marker='o',linewidth=0,alpha=1)
		else: continue

	if p_values[i] > 30 and 2**(-fold_changes[i]) > 10:
		plt.annotate(str(genes[i]+' '),(fold_changes[i],p_values[i]),fontsize=6,horizontalalignment='right',verticalalignment='center')


#Color points red if their fold-change (not log2(fold-change)) is larger than 10 (up or down) and their -log10(p-value) is above 8.

#Label points with their gene names if their fold-change (not log2(fold-change)) is larger than 10 (only down) and their -log10(p-value) is greater than 30.




plt.savefig('HW3_week7.pdf',transparent=True)















