import time
import board
import neopixel
import random
import sounddevice as sd
import numpy as np
import speech_recognition as sr

pixels = neopixel.NeoPixel(board.D21, 300)
r = sr.Recognizer()
m = sr.Microphone()
duration = 3

def print_sound(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*10
    
    #set vol threshold here
    if int(volume_norm) <= 10:
        pixels.fill((148, 0, 211))
        #print("purple2")
        
    elif int(volume_norm) <= 20:
        pixels.fill((75, 0, 130))
        #print("purple1")
        
    elif int(volume_norm) <= 41:
        pixels.fill((0, 0, 225))
        #print("blue")
        
    elif int(volume_norm) <= 83:
        pixels.fill((0, 255, 0))
        #print("green")
        
    elif int(volume_norm) <= 120:
        pixels.fill((255, 255, 0))
        #print("Yellow")
        
    elif int(volume_norm) <= 140:
        pixels.fill((255, 127, 0))
        #print("Orange")
        
    elif int(volume_norm) <= 165:
        pixels.fill((255, 0, 0))
        #print("Red")
        
    else:
        pixels.fill((0, 0, 0))
        #print("Lights off!")

while True:
    with sd.Stream(callback=print_sound):
        sd.sleep(duration * 1000)