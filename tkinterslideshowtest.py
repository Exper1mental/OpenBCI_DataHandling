#FOR REFERENCE: https://www.youtube.com/watch?v=iaQirRf2V7E&feature=youtu.be

import tkinter as tk
from PIL import Image, ImageTk
import random
import glob

class gui:
    #defines the main window, init takes two "_" per side, not one oops
    def __init__(self, mainwin):
        
        #A counter to find the data appended by pic function 
        self.counter = 0

        self.mainwin = mainwin
        self.mainwin.title('Tkinter Picture Frame')
        #zoomed makes it your full screen
        self.mainwin.state("zoomed")

        self.mainwin.configure(bg = 'yellow')
        #the frame is contained in the main window
        self.frame = tk.Frame(mainwin)
        #The self.img is the image acting as a lable in tk
        self.img = tk.Label(self.frame)
        self.img.pack()
        
        #Defines the relative size of the frame inside the window
        self.frame.place(relheight = 0.85, relwidth = 0.9, relx = 0.05, rely = 0.05)

        #runs the background color changer (if you want)
        self.color()
        
        self.pic()

    def color(self):
        self.colors = ['snow']

        c = random.choice(self.colors)
        self.mainwin.configure(bg = c)
        self.frame.config(bg = c)
        #repeats the change in background every 2000 milliseconds
        root.after(2000, self.color)

#pic function is for finding the pictures using "glob"
    def pic(self):

        self.pic_list = []

        #THE DIRECTORY WOULD HAVE TO BE CHANGED
        for name in glob.glob(r'A:\Files\2021\CI Information\Pictures\*'):
            val = name
            self.pic_list.append(val)

        if self.counter == len(self.pic_list) - 1:
            self.counter = 0
        else:
            self.counter = self.counter + 1
        
        self.file = self.pic_list[self.counter]
        self.load = Image.open(self.file)

        self.pic_width = self.load.size[0]
        self.pic_height = self.load.size[1]
        self.real_aspect = self.pic_width/self.pic_height

        self.cal_width = int(self.real_aspect * 800)

        self.load2 = self.load.resize((self.cal_width, 800))

        self.render = ImageTk.PhotoImage(self.load2)
        self.img.config(image = self.render)
        self.img.image = self.render

        #need to make it repeat for a specific number of times or for an amount of time
        root.after(2000, self.pic)

root = tk.Tk()
myprog = gui(root)
root.mainloop()
