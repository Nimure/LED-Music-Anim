import time
import board
import neopixel
import random

#print("hello blinky!")

pixels = neopixel.NeoPixel(board.D21, 300)

# pixels[0] = (255, 0, 0)

# while True:
#    pixels[0] = (255, 0, 0)
#    time.sleep(0.5)
#    pixels[0] = (0, 0, 0)
#    time.sleep(0.5)

 while True:
     pixels.fill((255, 0, 0))
     time.sleep(0.5)
     pixels.fill((255, 127, 0))
     time.sleep(0.5)
     pixels.fill((255, 255, 0))
     time.sleep(0.5)
     pixels.fill((0, 255, 0))
     time.sleep(0.5)
     pixels.fill((0, 0, 225))
     time.sleep(0.5)
     pixels.fill((75, 0, 130))
     time.sleep(0.5)
     pixels.fill((148, 0, 211))
     time.sleep(0.5)