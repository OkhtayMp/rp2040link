import time
from rp2040link import Pico

GP14, GP15 = 14, 15

with Pico() as pico:
    pico.setup_output.active_low(GP14, initial_off=True)
    pico.setup_output.active_high(GP15, initial_off=True)

    pico.gpio.on(GP14); time.sleep(0.5); pico.gpio.off(GP14)
    pico.gpio.on(GP15); time.sleep(0.5); pico.gpio.off(GP15)

    pico.gpio.blink([GP14, GP15], times=20, period_s=0.2)
