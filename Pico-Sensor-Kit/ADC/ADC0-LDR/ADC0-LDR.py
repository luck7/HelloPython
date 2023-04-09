from machine import Pin, ADC
import time
ldr_num = 26
ldr= ADC(Pin(ldr_num))

print("ldr Demo")
while True:
    voltage     = ldr.read_u16()*3.3/65535
    resistance  = ((10*3.3)/voltage)-10
    print("ldr voltage    = {0:.2f}V ".format(voltage))
    time.sleep(1)
                

