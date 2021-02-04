# Thomas Delvaux

# Importing Libraries
import matplotlib.pyplot as plt
import numpy as np
import PySimpleGUI as sg


# Importing Data
file_data = 'OpenBCI-RAW-2020-12-11_13-34-40.txt' #'OpenBCI-RAW Sample.txt'
file_data = 'processed_data_cyton.txt' #'cyton_data.txt'
#file_data = 'processed_data-OBCI.txt'


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


"""
# If using OpenBCI data
data_EEG = np.loadtxt(file_data, delimiter=', ', skiprows=6, dtype=str)

# If using BrainFlow data
#data_EEG = np.loadtxt(file_data, delimiter=',', skiprows=0, dtype=str) #np.loadtxt(file_data, delimiter=',', skiprows=1, dtype=float)
"""

row_rng_lo=500
row_rng_hi=None

#print(data_EEG[...,1])
#print('\n')
#print(data_EEG[row_rng_lo:row_rng_hi,1])

data_EEGch0 = data_EEG[row_rng_lo:row_rng_hi,1].astype(np.float)
data_EEGch1 = data_EEG[row_rng_lo:row_rng_hi,2].astype(np.float)
data_EEGch2 = data_EEG[row_rng_lo:row_rng_hi,3].astype(np.float)
data_EEGch3 = data_EEG[row_rng_lo:row_rng_hi,4].astype(np.float)
data_EEGch4 = data_EEG[row_rng_lo:row_rng_hi,5].astype(np.float)
data_EEGch5 = data_EEG[row_rng_lo:row_rng_hi,6].astype(np.float)
data_EEGch6 = data_EEG[row_rng_lo:row_rng_hi,7].astype(np.float)
data_EEGch7 = data_EEG[row_rng_lo:row_rng_hi,8].astype(np.float)

data_EEGtime = data_EEG[row_rng_lo:row_rng_hi,22].astype(np.float)

data_EEGtime = data_EEGtime - data_EEGtime[0]

print(data_EEGtime)

def plot_data():
    # Plotting Data
    plt.subplot(811)
    #plt.plot(data_EEGtime,data_EEGch0, 'ro')
    plt.plot(data_EEGtime,data_EEGch0, 'y-', markersize=2.0)

    plt.subplot(812)
    plt.plot(data_EEGtime,data_EEGch1, 'm-', markersize=2.0)

    plt.subplot(813)
    plt.plot(data_EEGtime,data_EEGch2, 'c-', markersize=2.0)

    plt.subplot(814)
    plt.plot(data_EEGtime,data_EEGch3, 'r-', markersize=2.0)

    plt.subplot(815)
    plt.plot(data_EEGtime,data_EEGch4, 'g-', markersize=2.0)
    plt.ylabel('Volts (V) [uV]')

    plt.subplot(816)
    plt.plot(data_EEGtime,data_EEGch5, 'b-', markersize=2.0)

    plt.subplot(817)
    plt.plot(data_EEGtime,data_EEGch6, 'k-', markersize=2.0)

    plt.subplot(818)
    plt.plot(data_EEGtime,data_EEGch7, 'y-', markersize=2.0)
    plt.xlabel('Time (t) [s]')

    plt.subplots_adjust(top=0.95,bottom=0.05,hspace=0.5)
    #plt.setp('markersize', 1.0)

    plt.show()



# Creating GUI
layout = [[sg.Text('Would you like to keep (Y) or discard (N) this data?')], [sg.Button('Yes'), sg.Button('No'), sg.Button('Plot Data'), sg.Button('Exit')]]

# Create the window
window = sg.Window('Question', layout)

# Create an event loop
while True:
    event, values = window.read()
    print(event)
    #print(values)
    
    # End program if user closes window or presses the OK button
    if event == 'Plot Data':
        plot_data()
    elif event == 'Yes':
        plt.close()
    elif event == 'No':
        plt.close()
    elif event == sg.WIN_CLOSED or event == 'Exit':
        plt.close()
        break
window.close()


"""
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()
"""