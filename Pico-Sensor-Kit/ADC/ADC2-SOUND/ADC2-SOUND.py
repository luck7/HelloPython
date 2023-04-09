from machine import Pin, ADC
import time

sound_aout_num = 28
sound_aout = ADC(Pin(sound_aout_num))

sound_dout_num = 21
sound_dout = Pin(sound_dout_num,Pin.IN)

print("sound aout demo")
while True:
    voltage     = sound_aout.read_u16()*3.3/65535
    print("sound aout voltage    = {0:.2f}V ".format(voltage))
    print("sound dout = {} ".format(sound_dout.value()))
    time.sleep_ms(300)
                

