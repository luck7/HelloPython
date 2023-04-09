from machine import Pin
import time

key_num = 3
key = Pin(key_num,Pin.IN,Pin.PULL_UP)

print("Wait for the key to be pressed")

while True:
    if(key.value() == 0): 
        time.sleep_ms(5)
        if(key.value() == 0): 
            print("The key is pressed")
            cnt=0
            while (key.value() == 0):
                cnt=cnt+1
                time.sleep_ms(1)        
            print("The key was held down {} ms".format(cnt))
                
