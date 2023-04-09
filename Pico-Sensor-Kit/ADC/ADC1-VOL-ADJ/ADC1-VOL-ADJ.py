from machine import Pin, ADC
import time
vol_adj_num = 27
vol_adj= ADC(Pin(vol_adj_num))

print("vol adj demo")
while True:
    voltage     = vol_adj.read_u16()*3.3/65535
    print("vol adj voltage    = {0:.2f}V ".format(voltage))
    time.sleep(1)
                

