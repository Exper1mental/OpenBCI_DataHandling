# Thomas Delvaux
# Data Handling for OpenBCI EEG data

import numpy as np
import math
#import pandas as pd

#file_data = 'OpenBCI-RAW Sample.txt'
#file_data = 'dummyfile.txt'
file_data = 'cyton_data.txt'
file_time = 'DataTime.txt'

# Try Importing As OpenBCI data
data_EEG = np.loadtxt(file_data, delimiter=', ', skiprows=5, dtype=str)
#print(data_EEG)

# Check if Data Successfully Imported
try:
    col = np.size(data_EEG,1)
# If Error, Try Importing As Brainflow data
except IndexError:
    data_EEG = np.loadtxt(file_data, delimiter=',', skiprows=0, dtype=str) #np.loadtxt(file_data, delimiter=',', skiprows=1, dtype=float)
    
    # Check if data successfully imported
    try:
        col = np.size(data_EEG,1)
    # If error, raise error and stop code
    except:
        raise Exception('Sorry, data could not be found in the file specified.')
    #print(data_EEG)

# Pull Out EEG Timestamps
time_EEG = data_EEG[...,22].astype(np.float)

# Image Timestamp Data
data_image = np.loadtxt(file_time, delimiter='\t| ', skiprows=2, dtype=str)
time_image = data_image[...,1].astype(np.float)

# Obtain Initial Time of EEG Data Collection
time_0_EEG = data_EEG[0,22]

#print(data_EEG[0,22])

#print(data_EEG[0,22])
#print(time_EEG)

# Spread Out Datapoints
rows = np.size(data_EEG,0)
print('Columns: '+str(col)+'\n'+'Rows: '+str(rows)+'\n')

i = 0
i_max = math.floor(rows/120)
#for i to 
#set_prev = 120*i-1 
set_min = 120*(i) # current set start row
set_max = 120*(i+1) # current set end row

set_time_EEG = np.linspace(time_EEG[set_min], time_EEG[set_max], num=120)

print(time_EEG[set_min])
print(time_EEG[set_max])
print(set_time_EEG)

#time_min = 
#time_max = 

#if math.floor(rows/120) != rows/120:
#

# Remove Initial Row from EEG Data
data_EEG = np.delete(data_EEG,0,0)
time_EEG = np.delete(time_EEG,0,0)


"""
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

"""
a = range(len(time_image))
print(a)
for i in a:
    print(i)
"""

k = 0

#new_EEG = np.empty([1,24])

for i in range(len(time_image)):
    if (i % 2) != 0:
        continue # skip 'finished' timestamps
    for j in range(len(time_EEG)):
        #if time_image[i] < time_EEG[j] and time_image[i] - time_EEG[j] < 0.5:
        if abs(time_image[i] - time_EEG[j]) < 0.1:
            # also need to check if next 3 seconds of data is continuous
            # 
            """
            try:
                new_EEG = np.append([data_EEG],[data_EEG[i:i+3,...]])
            except ValueError:
                new_EEG = data_EEG[i:i+3,...]
            """
            k = k + 1
            savename = 'cytondata' + str(k) + '.txt'

            np.savetxt(savename,data_EEG[i:i+5,...],delimiter=',',fmt="%s")

            #print('BAAMMM')
            print(str(time_image[i])+' - '+str(time_EEG[j])+' = '+str(time_image[i] - time_EEG[j]))
            break
        #print(str(i)+'\t'+str(j))
    #print(i)
#print(new_EEG)

#t2 = data_image[0:2,...]
#print(t2)

# Print entire array
#print(data_EEG)

# Print first row
# print(data[1,...])