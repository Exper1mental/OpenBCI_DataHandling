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

# Import Command Line Arguments
def commandLineSetup():
    commandParser = argparse.ArgumentParser(description="Opens a window with the "
                                                  "specified image")
    commandParser.add_argument("-i", "--imagefile", help="Name/Path of the image file")
    commandParser.add_argument("-n", "--imagename", help="Descriptive name the image")

    args = commandParser.parse_args()

    return args.imagefile, args.imagename

def main():
    imagefile, imagename = commandLineSetup()

    ### Image Window
    # ONLY SUPPORTS PNG and GIF. NO JPG SUPPORT.
    img_file = sg.Image(filename=imagefile, size=(3000, 1700), key='-IMAGE-')
    layout = [[img_file]]

    # Create the window
    window = sg.Window(imagename, layout)
    event, values = window.read()
    #print(event, values)

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == sg.WIN_CLOSED:
            break

    window.close()

main()