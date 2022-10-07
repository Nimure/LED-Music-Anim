import time
import board
import neopixel
import random

#print("hello blinky!")

pixels = neopixel.NeoPixel(board.D21, 300)

# pixels[0] = (255, 0, 0)

 while True:
    pixels[0] = (255, 0, 0)
    time.sleep(0.5)
    pixels[0] = (0, 0, 0)
    time.sleep(0.5)