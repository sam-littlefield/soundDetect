import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import pyautogui
import pyscreenshot as ImageGrab
import time
import pyaudio
import wave
from array import array
import keyboard
import mouse
import time
import random

time.sleep(2)
def bobberfish():
    a=0
    b=0
    for i in range(1350, 1550, 100):
        a+=1
        for c in range(350, 650, 100):
            b+=1
            im=ImageGrab.grab(bbox=(0,0,2560,1440))
            im.save('./ImageInImage/assets/im'+str(a+b)+'.png')
            # Image we want to search
            img_rgb = cv.imread('./ImageInImage/assets/im'+str(a+b)+'.png')
            # Make image grey to remove some variation
            img_grey = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
            # Image we want to find
            template = cv.imread('./ImageInImage/assets/cog2.png',0)
            # Match grey image to template
            w, h = template.shape[::-1]
            res = cv.matchTemplate(img_grey,template,cv.TM_CCOEFF_NORMED)
            
            # Set rules for what counts as a match
            threshold = 0.8
            loc = np.where( res >= threshold)
            
            # Draw red box around the item we think matches
            for pt in zip(*loc[::-1]):
                cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
                FORMAT=pyaudio.paInt16
                CHANNELS=2
                RATE=random.randint(2000, 5000)
                CHUNK=1024
                RECORD_SECONDS=1500
                FILE_NAME="RECORDING.wav"

                audio=pyaudio.PyAudio() #instantiate the pyaudio

                #recording prerequisites
                stream=audio.open(format=FORMAT,channels=CHANNELS, 
                                  rate=RATE,
                                  input=True,
                                  frames_per_buffer=CHUNK)

                #starting recording
                frames=[]
                for i in range(0,int(RATE/CHUNK*RECORD_SECONDS)):
                    data=stream.read(CHUNK)
                    data_chunk=array('h',data)
                    vol=max(data_chunk)
                    if(vol>=1500):
                        print("something said")
                        keyboard.press('shift')
                        mouse.click(button='right')
                        keyboard.release('shift')
                        return                    
                    else:
                        print("nothing")



            # Write image with red box to file
            cv.imwrite('./ImageInImage/assets/foundCog.png',img_rgb)
            
            pyautogui.moveTo(i, c)

while True:
    keyboard.press_and_release('1')
    bobberfish()
    time.sleep(5)
    
        









