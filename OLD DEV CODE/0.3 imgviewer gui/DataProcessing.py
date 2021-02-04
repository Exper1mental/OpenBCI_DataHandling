# Thomas Delvaux
# Data Handling for OpenBCI EEG data

import numpy as np
import pandas as pd

#file_data = 'OpenBCI-RAW Sample.txt'
file_data = 'cyton_data.txt'
file_time = 'DataTime.txt'

# If using OpenBCI data
#data_EEG = np.loadtxt(file_data, delimiter=', ', skiprows=6, usecols=[22,23], dtype=str)
#time_EEG = data_EEG[...,0].astype(np.float)

# If using BrainFlow data
data_EEG = np.loadtxt(file_data, delimiter=',', skiprows=1, usecols=[22], dtype=float)
time_EEG = data_EEG

# Image Timestamp Data
data_image = np.loadtxt(file_time, delimiter='\t| ', skiprows=2, dtype=str)
time_image = data_image[...,1].astype(np.float)

print(time_EEG)
print('\n')
print(time_image)

if time_EEG[0] < time_EEG[1]:
    print('yes\n')
    print(time_EEG[0])
    print(time_EEG[-1])
    print('\n')
    print(time_image[0])
    print(time_image[-2])

print(len(time_image))

"""
a = range(len(time_image))
print(a)
for i in a:
    print(i)
"""

new_EEG = []

for i in range(len(time_image)):
    if (i % 2) != 0:
        continue # skip 'finished' timestamps
    for j in range(len(time_EEG)):
        #if time_image[i] < time_EEG[j] and time_image[i] - time_EEG[j] < 0.5:
        if abs(time_image[i] - time_EEG[j]) < 0.1:
            new_EEG = np.append(data_EEG,data_EEG[i:i+3,...])
            print('BAAMMM')
            print(str(time_image[i])+' - '+str(time_EEG[j])+' = '+str(time_image[i] - time_EEG[j]))
            break
        #print(str(i)+'\t'+str(j))
    print(i)
print(new_EEG)

#t2 = data_image[0:2,...]
#print(t2)

# Print entire array
#print(data_EEG)

# Print first row
# print(data[1,...])