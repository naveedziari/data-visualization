import argparse 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mplpatches
import matplotlib.image as img
import math
import random
import sys
from collections import Counter
import operator

plt.style.use('BME163.mplstyle.txt')

figure_width=6
figure_height=3

plt.figure(figsize=(figure_width,figure_height))

panel_width=1/figure_width
panel_height=1/figure_height

# panel_width,panel_height = 2.4, 1

panel1=plt.axes([0.5/6,0.3,panel_width*2.4,panel_height])
panel2=plt.axes([(2.4+1)/6,0.3,panel_width*2.4,panel_height])

panel1.set_xlim([0, 20])
panel2.set_xlim([0, 20])
panel2.set_yticks([],[])
panel1.set_ylim([0,2])
panel2.set_ylim([0,2])

panel1.set_ylabel('Bits')
panel1.set_xlabel('Distance to\nSplice Site')
panel2.set_xlabel('Distance to\nSplice Site')

panel1.plot([10 for i in range(10)],list(range(0,10)),color='black',linewidth=0.5)
panel2.plot([10 for i in range(10)],list(range(0,10)),color='black',linewidth=0.5)

panel1.set_title('5\'SS')
panel2.set_title('3\'SS')

def rev_comp(s): return ''.join([{'A':'T','C':'G','G':'C','T':'A'}[B] for B in s][::-1])
        
class FastAreader :	
	def __init__ (self, fname): self.fname = fname 
	def doOpen (self):
		if self.fname is '': return sys.stdin
		else: return open(self.fname) 
	def readFasta (self):
		header,sequence = '',''
		with self.doOpen() as fileH:			
		    header,sequence = '',''
		    line = fileH.readline()
		    while not line.startswith('>') : line = fileH.readline()
		    header = line[1:].rstrip()
		    for line in fileH:
		        if line.startswith ('>'):
		            yield header,sequence
		            header = line[1:].rstrip()
		            sequence = ''
		        else : sequence += ''.join(line.rstrip().split()).upper()						
		yield header,sequence


A = img.imread('A_small.png')
T = img.imread('T_small.png')
C = img.imread('C_small.png')
G = img.imread('G_small.png')
image_dict = {'A':A, 'T':T, 'C':C,'G':G}

reader_obj = FastAreader('Mus_musculus.GRCm38.dna.primary_assembly.fa')
reader_obj.doOpen()
sequence_dict = {}

for header, sequence in reader_obj.readFasta():
	if (header[0] != 'J') and (header[0] != 'G'):
		chromosome = 'chr'+header.split(' ')[0]
		if chromosome == 'chrMT': chromosome = chromosome[:-1]
		sequence_dict.update({chromosome:sequence})

array_3 = []
array_5 = []
counter_3 = True
counter_5 = True
for line in open('Splice_Locations.bed.txt'):
	a = line.strip().split('\t')
	chromosome = str(a[0])
	splice_direction = str(a[3][0])
	#print(splice_direction)

	position = int(a[1])
	temp_sequence = sequence_dict[chromosome][(position-10):(position+10)].upper()

	if splice_direction == '3':
		temp_sequence = rev_comp(temp_sequence)
		array_3.append(temp_sequence)
	else: 
		array_5.append(temp_sequence)



dict_5 = {i:[] for i in range(20)}
dict_3 = {i:[] for i in range(20)}
for sequence in array_5:
	for position in range(20):
		dict_5[position].append(sequence[position])

for sequence in array_3:
	for position in range(20):
		dict_3[position].append(sequence[position])	




for base in list(dict_5.keys()):
	H_5 = 0
	frequencies = Counter(dict_5[base])
	print(frequencies)
	for i,j in frequencies.items():
		frequencies[i] = float(j/len(dict_5[base]))
		H_5 += -frequencies[i] * np.log2(frequencies[i])
	R_5 = 2.0 - H_5

	height = 0
	for key,value in sorted(frequencies.items(),key = lambda item: item[1]):
		panel1.imshow(image_dict[key],extent = [base,base+1,height,height+(frequencies[key]*R_5)],aspect = 'auto')
		height = height + (frequencies[key]*R_5)




for base in list(dict_3.keys()):
	H_3 = 0
	frequencies = Counter(dict_3[base])
	for i,j in frequencies.items():
		frequencies[i] = float(j/len(dict_3[base]))
		H_3 += -frequencies[i] * np.log2(frequencies[i])
	R_3 = 2.0 - H_3

	height = 0

	for key,value in sorted(frequencies.items(), key = lambda item: item[1]):
		panel2.imshow(image_dict[key],extent = [base,base+1,height,height+(frequencies[key]*R_3)],aspect = 'auto')
		height = height + (frequencies[key]*R_3)


panel1.set_xticklabels([-10,-5,0,5,10])
panel2.set_xticklabels([-10,-5,0,5,10])


plt.savefig('HW5.png')


















