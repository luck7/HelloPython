import errno
from sys import platform
import time
import gc
from machine import Pin, freq
from ir_rx.nec import NEC_8, NEC_16, SAMSUNG
ir_rx_num=15
if platform == "rp2":
    ir_pin = Pin(ir_rx_num, Pin.IN)
print("ir rx demo(nec 16bit)")
# User callback
def ir_callback(data, addr, ctrl):
    if data < 0:  # NEC protocol sends repeat codes.
        print("Repeat code.")
    else:
        print(f"Data 0x{data:02x} Addr 0x{addr:04x} Ctrl 0x{ctrl:02x}")

ir=NEC_16(ir_pin,ir_callback)

while True:
    pass