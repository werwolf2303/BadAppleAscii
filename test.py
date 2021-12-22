import PIL.Image
import threading
import time
import pyautogui
import os
import fpstimer

def thre():
 ima = 1
 #limit it to 30fps
 timer = fpstimer.FPSTimer(30)
 while (True):
   image_path = "frames/" + str(ima) + ".bmp"
   img = PIL.Image.open(image_path)
   # resize the image
   width, height = img.size
   aspect_ratio = height / width
   new_width = 120
   new_height = aspect_ratio * new_width * 0.55
   width, height = pyautogui.size()
   x,y = pyautogui.size()
   img = img.resize((new_width,int(new_height)))
   # new size of image
   # print(img.size)

   # convert image to greyscale format
   img = img.convert('L')
   pixels = img.getdata()

   # replace each pixel with a character from array
   chars = [".", "-", "+", "*", "w", "G", "H", "M", "#", "&", "%"]
   new_pixels = [chars[pixel // 25] for pixel in pixels]
   new_pixels = ''.join(new_pixels)

   # split string of chars into multiple strings of length equal to new width and create a list
   new_pixels_count = len(new_pixels)
   ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
   ascii_image = "\n".join(ascii_image)
   print(ascii_image.replace(".", " "))
   ima = ima + 1
   timer.sleep()

t = threading.Thread(target=thre)
t.start()
from playsound import playsound

# Input an existing wav filename
wavFile = "audio.wav"
# Play the wav file
playsound(wavFile)
