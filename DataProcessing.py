# Thomas Delvaux
# Data Handling for OpenBCI EEG data

import numpy as np
import math
#import pandas as pd

file_data = 'OpenBCI-RAW-2020-12-11_13-34-40.txt' # 'OpenBCI-RAW Sample.txt'
#file_data = 'dummyfile.txt'
#file_data = 'cyton_data.txt'
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
time_0_EEG = time_EEG[0] #data_EEG[0,22]

#print(data_EEG[0,22])

#print(data_EEG[0,22])
#print(time_EEG)

# Spread Out Datapoints
rows = np.size(data_EEG,0)
print('Columns: '+str(col)+'\n'+'Rows: '+str(rows)+'\n')

i_max = math.floor(rows/120)
set_time_EEG = []
i_prev = 0
gap_index = []
gap_time_i = []
gap_time_f = []

for i in range(rows-1): #242): # skip first row
    if i == 0:
        gap_index = np.append(gap_index, i)
    elif time_EEG[i+1] - time_EEG[i] > 0.1:
        gap_index = np.append(gap_index, i)
        #gap_time_i = np.append(gap_time_i, time_EEG[i-1])
        #gap_time_f = np.append(gap_time_f, time_EEG[i])

# Append time for remaining data samples.
gap_index = np.append(gap_index,rows-1)

#print(np.linspace(0,3,num=2,endpoint=False))

time_EEG1 = time_EEG

print(gap_index)

for j in range(np.size(gap_index)-1):
    num_rng = int(gap_index[j+1]-gap_index[j])

    ini = int(gap_index[j])
    ini_time = time_EEG[ini]
    #print(ini_time)

    fin = int(gap_index[j+1])
    fin_time = time_EEG[fin]
    #print(fin_time)

    #print(np.linspace((ini_time-time_0_EEG), (fin_time-time_0_EEG), num=num_rng, endpoint=True))
    set_time_EEG = np.append(set_time_EEG, np.linspace(ini_time, fin_time, num=num_rng, endpoint=False))
    set_time_EEG_zeroed = np.linspace(0, fin_time-ini_time, num=num_rng)

#print(set_time_EEG[-1])

set_time_EEG = np.append(set_time_EEG, time_EEG[-1])

#print(set_time_EEG[-1])
#print(j)
print(set_time_EEG.astype(str))
#print(set_time_EEG_zeroed)

"""
for i in range(0,rows): # skip first row
    if time_EEG[i] - time_EEG[i-1] > 0.1:
        for j in range(i,rows):
            
        if i_prev == 0:
            i_prev = i
        else:
            set_time_EEG = np.append(set_time_EEG, np.linspace(time_EEG[i-1], time_EEG[i], num=120, endpoint='false'))
            set_time_EEG_zeroed = np.linspace(0, time_EEG[set_max]-time_EEG[set_min], num=120)
"""

print(np.size(set_time_EEG))


#set_time_EEG
#data_EEG 


#print(time_EEG[set_min])
#print(time_EEG[set_max])
#print(set_time_EEG)
#print(set_time_EEG_zeroed)
#print(set_time_EEG.astype(str))
#time_EEG = 

data_EEG[...,22] = set_time_EEG.astype(str)
time_EEG = set_time_EEG
#print(data_EEG)



# Remove Initial Row from EEG Data
data_EEG = np.delete(data_EEG,0,0)
time_EEG = np.delete(time_EEG,0,0)

#print(time_EEG.astype(str))

k = 0

#new_EEG = np.empty([1,24])

savename = 'processed_data-OBCI.txt'
np.savetxt(savename,data_EEG,delimiter=',',fmt="%s")

"""
for i in range(len(time_image)):
    if (i % 2) != 0:
        continue # skip 'finished' timestamps
    for j in range(len(time_EEG)):
        #if time_image[i] < time_EEG[j] and time_image[i] - time_EEG[j] < 0.5:
        if abs(time_image[i] - time_EEG[j]) < 0.005:
            # also need to check if next 3 seconds of data is continuous
            # 
            k = k + 1
            savename = 'cytondata' + str(k) + '.txt'

            np.savetxt(savename,data_EEG[i:i+120,...],delimiter=',',fmt="%s")

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
"""