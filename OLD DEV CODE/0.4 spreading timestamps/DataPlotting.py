# Thomas Delvaux

# Importing Libraries
import matplotlib.pyplot as plt
import numpy as np
import PySimpleGUI as sg


# Importing Data
file_data = 'OpenBCI-RAW-2020-11-13_03-54-33.txt' #'OpenBCI-RAW Sample.txt'
#file_data = 'cyton_data.txt'

# If using OpenBCI data
data_EEG = np.loadtxt(file_data, delimiter=', ', skiprows=6, dtype=str)

# If using BrainFlow data
#data_EEG = np.loadtxt(file_data, delimiter=',', skiprows=1, dtype=str) #np.loadtxt(file_data, delimiter=',', skiprows=1, dtype=float)

data_EEGch0 = data_EEG[...,1].astype(np.float)
data_EEGch1 = data_EEG[...,2].astype(np.float)
data_EEGch2 = data_EEG[...,3].astype(np.float)
data_EEGch3 = data_EEG[...,4].astype(np.float)
data_EEGch4 = data_EEG[...,5].astype(np.float)
data_EEGch5 = data_EEG[...,6].astype(np.float)
data_EEGch6 = data_EEG[...,7].astype(np.float)
data_EEGch7 = data_EEG[...,8].astype(np.float)

data_EEGtime = data_EEG[...,22].astype(np.float)

data_EEGtime = data_EEGtime - data_EEGtime[0]

print(data_EEGtime)

def plot_data():
    # Plotting Data
    plt.subplot(811)
    #plt.plot(data_EEGtime,data_EEGch0, 'ro')
    plt.plot(data_EEGtime,data_EEGch0, 'yo', markersize=2.0)

    plt.subplot(812)
    plt.plot(data_EEGtime,data_EEGch1, 'mo', markersize=2.0)

    plt.subplot(813)
    plt.plot(data_EEGtime,data_EEGch2, 'co', markersize=2.0)

    plt.subplot(814)
    plt.plot(data_EEGtime,data_EEGch3, 'ro', markersize=2.0)

    plt.subplot(815)
    plt.plot(data_EEGtime,data_EEGch4, 'go', markersize=2.0)
    plt.ylabel('Y-Label (-) [-]')

    plt.subplot(816)
    plt.plot(data_EEGtime,data_EEGch5, 'bo', markersize=2.0)

    plt.subplot(817)
    plt.plot(data_EEGtime,data_EEGch6, 'ko', markersize=2.0)

    plt.subplot(818)
    plt.plot(data_EEGtime,data_EEGch7, 'yo', markersize=2.0)
    plt.xlabel('Time (t) [s]')

    plt.subplots_adjust(top=0.95,bottom=0.05,hspace=0.5)
    #plt.setp('markersize', 1.0)

    plt.show()



# Creating GUI
layout = [[sg.Text('Would you like to keep (Y) or discard (N) this data?')], [sg.Button('Yes'), sg.Button('No'), sg.Button('Plot Data')]]

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