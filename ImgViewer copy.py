# Thomas Delvaux
# Based on code from:
# https://realpython.com/pysimplegui-python/

# And Documentation from
# https://pysimplegui.readthedocs.io/en/latest/call reference/#image-element

# from skimage.viewer import ImageViewer
# from skimage.io import imread

# img = imread('1200pxBanana-Single.jpg') #path to IMG
# view = ImageViewer(img)
# view.show()

# Import the necessary libraries
import PySimpleGUI as sg
import argparse
#import time


### Apple Window
# ONLY SUPPORTS PNG and GIF. NO JPG SUPPORT.
img_file = sg.Image(filename="1200px-Apple.png", size=(3000, 1700), key='-IMAGE-')
layout = [[img_file], [sg.Button('Show')]]
            #[[sg.Text("Hello from PySimpleGUI")], [sg.Button("OK")]]

# Create the window
window = sg.Window("Apple", layout)
event, values = window.read()
print(event, values)

# wait for a period of time
#secs = 3
#time.sleep(secs)



### Banana Window
#window['-IMAGE-'].Update(filename="1200px-Banana.png")
#event, values = window.read()
# ONLY SUPPORTS PNG and GIF. NO JPG SUPPORT.
#layout = [[sg.Image(filename="1200px-Banana.png", size=(3000, 1700))]]
            #[[sg.Text("Hello from PySimpleGUI")], [sg.Button("OK")]]

# Create the window
#window = sg.Window("Banana", layout)

# wait for a period of time
#secs = 3
#time.sleep(secs)


# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == sg.WIN_CLOSED:
        break

window.close()