# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685

import random as rnd

# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 150  # 150 Min pulse length out of 4096
servo_max = 600  # 600 Max pulse length out of 4096

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

def open_all():
    pwm.set_pwm(1, 0, 600)
    pwm.set_pwm(3, 0, 600)
    pwm.set_pwm(5, 0, 600)
    pwm.set_pwm(2, 0, 400)
    pwm.set_pwm(4, 0, 400)
    pwm.set_pwm(6, 0, 400)
    time.sleep(2)

def close_all():
    pwm.set_pwm(1, 0, 450)
    pwm.set_pwm(3, 0, 450)
    pwm.set_pwm(5, 0, 450)
    pwm.set_pwm(2, 0, 150)
    pwm.set_pwm(4, 0, 150)
    pwm.set_pwm(6, 0, 150)

def reset1():
    pwm.set_pwm(0, 0, 150) 
    pwm.set_pwm(1, 0, 150)
    pwm.set_pwm(3, 0, 150)
    pwm.set_pwm(5, 0, 150)
    pwm.set_pwm(2, 0, 150)
    pwm.set_pwm(4, 0, 150)
    pwm.set_pwm(6, 0, 150)

open_all()
close_all()
#reset1()