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
        
    if int(volume_norm) <= 1:
        pixels.fill((0, 0, 0))
        #print("off")
        
    elif int(volume_norm) <= 5:
        pixels.fill((0, 0, 225))
        #print("blue")
        
    elif int(volume_norm) <= 15:
        pixels.fill((0, 255, 0))
        #print("green")
        
    elif int(volume_norm) <= 25:
        pixels.fill((255, 255, 0))
        #print("Yellow")
        
    elif int(volume_norm) <= 35:
        pixels.fill((255, 127, 0))
        #print("Orange")
        
    elif int(volume_norm) <= 45:
        pixels.fill((255, 0, 0))
        #print("Red")
        
    else:
        pixels.fill((0, 0, 0))
        #print("Lights off!")

while True:
    with sd.Stream(callback=print_sound):
        sd.sleep(duration * 1000)
    #print("loop")