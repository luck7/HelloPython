from machine import Pin
import time

led_num = 10
led = Pin(led_num,Pin.OUT)

print("led demo")

while True:
    led.toggle()
    time.sleep_ms(500)
                
