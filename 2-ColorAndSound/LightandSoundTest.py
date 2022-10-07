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
    if int(volume_norm) > 10:
        pixels.fill((255, 0, 0))
        print("Lights on!")
        
    else:
        pixels.fill((0, 0, 0))
        print("Lights off!")

while True:
    with sd.Stream(callback=print_sound):
        sd.sleep(duration * 1000)
    print("loop")