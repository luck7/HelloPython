from machine import Pin,PWM
import time

buzzer_num = 12
buzzer_start_freq = 600
buzzer_end_freq   = 1400 

buzzer = PWM(Pin(buzzer_num))
buzzer.freq(10)
buzzer_duty = 30
buzzer.duty_u16(int(buzzer_duty * 655.36))
print("buzzer demo")
while True:
    for cnt in range(buzzer_start_freq,buzzer_end_freq,10):
        buzzer.freq(cnt)
        time.sleep_ms(10)
    for cnt in range(buzzer_end_freq,buzzer_start_freq,-10):
        buzzer.freq(cnt)
        time.sleep_ms(10)
                
