# https://www.geeksforgeeks.org/working-images-python/

# On psutil
# https://github.com/giampaolo/psutil

from PIL import Image
import time
import psutil

#img  = Image.open(path)      
# On successful execution of this statement, 
# an object of Image type is returned and stored in img variable) 
   
try:  
    img  = Image.open('1200px-Banana.png')  
    img.show()
    ptime.sleep(3)
    img.close()
    for proc in psutil.process_iter():
        if proc.name() == "Microsoft.Photos.exe":
            proc.kill()
except IOError: 
    pass
# Use the above statement within try block, as it can  
# raise an IOError if file cannot be found,  
# or image cannot be opened.