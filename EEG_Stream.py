# Based on
# https://towardsdatascience.com/creating-an-ecg-data-stream-with-openbci-device-52d89206f272

# Dependencies
import openBCIStream  ## openBCIStream already imports Brainflow
import matplotlib.pyplot as plt
import pandas as pd
import time
from datetime import datetime
## The dongle for Cyton is plugged in at the serial port 
## "/dev/ttyUSB0" in the Ubuntu OS

# Useful function for logging
def timestamp():
    return datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

# Connecting
cytonBoard = openBCIStream.CytonBoard("COM5")

# Streaming
cytonBoard.start_stream()

# Polling
ecg = [] ## List to store ECG values
n = 250
plt.style.use("ggplot")
fig = plt.figure(figsize=(15, 6))
ax = fig.add_subplot()
fig.show()


i = 0
while plt.fignum_exists(fig.number): #True:
    df_ecg = cytonBoard.poll(250)  ## Polling for 250 samples
    ecg.extend(df_ecg.iloc[:, 0].values)  ## extracting ECG values 
    ## Making the plot dynamic with autoscaling and x-axis shifter
    plt.autoscale(enable=True, axis="y", tight=True)
    ax.plot(ecg, color="r")
    fig.canvas.draw()
    fig.canvas.flush_events()
    ax.set_xlim(left=n - 250, right=n)
    n = n + 250
    time.sleep(1)  ## Updating the window in every one second
    
    #print(df_ecg)
    #print("\n")
    #print(ecg)

# Saving Data
cytonBoard.save_data()

# Stopping Stream
cytonBoard.stop_stream()

# Continue to show plot until user closes window
plt.show()