import neopixel
import random

print("hello blinky!")

pixels = neopixel.NeoPixel(board.D21, 300)

pixels[0] = (255, 0, 0)