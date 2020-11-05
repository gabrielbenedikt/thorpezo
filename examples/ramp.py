#!/usr/bin/env python3

import thorpezo as t
import time
import numpy as np

def ramp(dev, volts, delay):
    dev.ignore_serial_read(True)
    dev.ser.timeout=0.0001
    for v in volts:
        dev.set_xvolt(v)
        time.sleep(delay)
    time.sleep(0.01)
    dev.ignore_serial_read(False)
    dev.ser.timeout=0.01

vlist=np.linspace(0,100,10001)

i=t.Thorpezo('/dev/ttyACM0')

p=i.device

p.msg('id?')

ramp(p, vlist,0.0001)
