import time
import board
import neopixel
import random
import speech_recognition as sr

pixels = neopixel.NeoPixel(board.D21, 300)
r = sr.Recognizer()
m = sr.Microphone()

try:
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    while True:
        print("Say something!")
        with m as source: audio = r.listen(source)
        print("Turning on Lights")
        try:
            def set_pixel_with_delay(position, color):
                pixels[position] = color
                time.sleep(0.2)
                pixels[position] = (0, 0, 0)
 
            if __name__ == '__main__':

                #Define colors
                R = (255, 0, 0)
                O = (255, 127, 0)
                Y = (255, 255, 0)
                G = (0, 255, 0)
                B = (0, 0, 225)
                P1 = (75, 0, 130)
                P2 = (148, 0, 211)

                #define pattern
                color_pattern_loop = [R, O, Y, G, B, P1, P2]
    
                pixel_position = 0
                color_array_position = 0
    
                while True:

                    set_pixel_with_delay(pixel_position, color_pattern_loop[color_array_position])

                    pixel_position += 1
                    color_array_position += 1

                    # Reset to 0 if it goes more than the range we want
                    if pixel_position > 10:
                        pixel_position = 0

                   # If it gets set to bigger than the size of the color_pattern_loop then start over at beginning
                    if color_array_position > 6:
                        color_array_position = 0
            
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
except KeyboardInterrupt:
    pass