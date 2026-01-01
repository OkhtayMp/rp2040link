import time
from rp2040link import Pico

GP14, GP15 = 14, 15

with Pico() as pico:
    pico.setup_output.active_low(GP14, initial_off=True)
    pico.setup_output.active_high(GP15, initial_off=True)

    # single pin
    b14 = pico.binary.pin(GP14)
    b14.pattern("101001", delay_s=0.05)

    # 2-pin bus
    bus = pico.binary.pins(GP14, GP15)
    bus.stream([0,1,2,3,2,1,0], delay_s=0.2)
