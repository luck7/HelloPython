import time
from machine import Pin
from neopixel import NeoPixel

max_lum =100

rgb_led_num =   22
rgb_led_pin =   Pin(rgb_led_num, Pin.OUT)
rgb_led     =   NeoPixel(rgb_led_pin, 1) 

red=0
green=0
blue=0
print("rgb led demo")
while True:
    for i in range(0,max_lum):
        red=i
        blue=max_lum-i
        rgb_led[0]=(red,green,blue)
        rgb_led.write()
        time.sleep_ms(10)
    time.sleep_ms(300)
    for i in range(0,max_lum):
        green=i
        red=max_lum-i
        rgb_led[0]=(red,green,blue)
        rgb_led.write()
        time.sleep_ms(10)
    time.sleep_ms(300)
    for i in range(0,max_lum):
        blue=i
        green=max_lum-i
        rgb_led[0]=(red,green,blue)
        rgb_led.write()
        time.sleep_ms(10)
    time.sleep_ms(300)