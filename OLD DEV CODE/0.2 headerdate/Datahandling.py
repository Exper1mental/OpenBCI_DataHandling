# Thomas Delvaux
# Data Handling for OpenBCI EEG data
# 11/13/2020

# Image import based on example from:
# https://pythonexamples.org/python-pillow-show-display-image/

# Time function info:
# https://www.pythoncentral.io/pythons-time-sleep-pause-wait-sleep-stop-your-code/


# Import necessary libraries
#from PIL import Image
import time
import subprocess
import PySimpleGUI as sg
import datetime as dt

# Define number of iterations to run
n = 2

## ADD second button to exit out of tests when in loop
## use while loop
## Could set size to be screen size

# Apple
imgfile_apple = "1200px-Apple.png"
imgname_apple = "Apple"
argstr_apple1 = '-i' + imgfile_apple
argstr_apple2 = '-n' + imgname_apple

# Banana
imgfile_banana = "1200px-Banana.png"
imgname_banana = "Banana"
argstr_banana1 = '-i' + imgfile_banana
argstr_banana2 = '-n' + imgname_banana


### Empty Window
# ONLY SUPPORTS PNG and GIF. NO JPG SUPPORT.
img_file = sg.Image(filename='1200px.png', size=(3000, 1700), key='-IMAGE-')
layout = [[img_file], [sg.Button('Start'), sg.Button('Exit')]]

# Create the window
window = sg.Window('Blank', layout)

# Create an event loop
while True:
    event, values = window.read()
    print(event)
    print(values)
    # End program if user closes window or
    # presses the OK button
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == 'Start':
        # Collect n sets of data
        for x in range(n):
            
            if x == 0:
                # Check if file exists / creates file to record data to
                with open('TimeStamps.txt', 'r') as file:
                    # file is now open / created
                    
                    # Check file for contents
                    file.seek(0) # ensure you're at the start of the file..
                    first_char = file.read(1) # get the first character
                
                # Adds file header if file is empty
                with open('TimeStamps.txt', 'a') as file:
                    if not first_char:
                        file.write('=== Autogenerated Timestamps ===\n'+\
                            'Date: %s\n' %dt.date.today())
            
            # wait for a period of time while showing blank image
            secs = 0.3
            time.sleep(secs)

            # record date/time and show apple image
            with open('TimeStamps.txt', 'a') as file:
                file.write('%s | %s Apple Start\n' %(dt.datetime.now().time(), x))

            p = subprocess.Popen(['python', 'ImgViewer.py', argstr_apple1, argstr_apple2])

            # wait for a period of time and kill process
            time.sleep(secs)
            p.kill()
            
            with open('TimeStamps.txt', 'a') as file:
                file.write('%s | %s Apple Finish\n' %(dt.datetime.now(), x))
            
            # wait for a period of time showing blank image
            time.sleep(secs)

            # record date/time and show banana image
            with open('TimeStamps.txt', 'a') as file:
                file.write('%s | %s Banana Start\n' %(dt.datetime.now(), x))
            
            p = subprocess.Popen(['python', 'ImgViewer.py', argstr_banana1, argstr_banana2])
                        # wait for a period of time and kill process
            time.sleep(secs)
            p.kill()
            
            with open('TimeStamps.txt', 'a') as file:
                file.write('%s | %s Banana Finish\n' %(dt.datetime.now(), x))


window.close()
