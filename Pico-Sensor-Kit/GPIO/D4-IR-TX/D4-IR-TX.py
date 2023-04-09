
from sys import platform
from machine import Pin

from ir_tx.nec import NEC
import time

addr = 0x01
data = 0x07

ir_rx_num = 16
key_num = 3
led_num = 10

try:
    key = Pin(key_num,Pin.IN,Pin.PULL_UP)
    led = Pin(led_num, Pin.OUT,value = 1)
    ir_rxpin = Pin(ir_rx_num, Pin.OUT, value = 0)
    irb = NEC(ir_rxpin, 38000,verbose = False)  # My decoder chip is 38KHz
    time.sleep(0.1)
    print("Wait for the key to be pressed")
    while True:
        if(key.value() == 0):
            led.value(0)
            irb.transmit(addr,data,0, True)
            print("The key is pressed")
            time.sleep(0.3)
            time_cnt = 0
            while(key.value() == 0):         
                irb.repeat()
                led.toggle()
                time.sleep(0.15)
                time_cnt=time_cnt+1
                print("pressed cnt = {}".format(time_cnt))
            led.value(1)
            print("The key  is released\r\n")
            print("--------------------------------------\r\n")
            print("Wait for the key to be pressed")
        time.sleep(0.01)
        
except:
    pass



