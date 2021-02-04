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
#img_file = sg.Image(filename="1200px-Apple.png", size=(3000, 1700), key='-IMAGE-')
layout = [[img_file], [sg.Button('Start')]]

# Create the window
window = sg.Window('Blank', layout)
#event, values = window.read()

# show apple image
#p = subprocess.Popen(['python', 'ImgViewer.py', argstr_apple1, argstr_apple2])
#p = subprocess.Popen('python ImgViewer.py')

# wait for a period of time and kill process
#secs = 3
#time.sleep(secs)
#p.kill()

#show banana image
#p = subprocess.Popen(['python', 'ImgViewer.py', argstr_banana1, argstr_banana2])


# wait for a period of time and kill process
#secs = 3
#time.sleep(secs)
#p.kill()

# Create an event loop
while True:
    event, values = window.read()
    print(event)
    print(values)
    # End program if user closes window or
    # presses the OK button
    if event == sg.WIN_CLOSED:
        break

    # show apple image
    p = subprocess.Popen(['python', 'ImgViewer.py', argstr_apple1, argstr_apple2])
    #p = subprocess.Popen('python ImgViewer.py')

    # wait for a period of time and kill process
    secs = 3
    time.sleep(secs)
    p.kill()

    #show banana image
    p = subprocess.Popen(['python', 'ImgViewer.py', argstr_banana1, argstr_banana2])


    # wait for a period of time and kill process
    secs = 3
    time.sleep(secs)
    p.kill()

window.close()
