#!/usr/bin/python3
# gpiozero - control DC motor
# 12/15/17
# updated: 12/15/17

import time
import numpy
from gpiozero import Motor


sleep_time = 0.05
interval = 21

# arange below results in: array([ 0. ,  0.1,  0.2,  0.3,  0.4,  0.5,  0.6,  0.7,  0.8,  0.9])
# steps = numpy.arange(0.0, 1.0, 0.1)
steps = numpy.linspace(0, 1, interval)


def ramp_up(motor, steps):
    for step in steps:
        motor.forward(speed=step)
        time.sleep(sleep_time)

    return step


def ramp_down(motor, steps):
    '''have to add 1 to because regular indexing starts @ 0, but reverse indexing starts @ -1'''

    for step in range(len(steps)):
        step += 1
        step *= -1
        motor.forward(speed=steps[step])
        time.sleep(sleep_time)

    return step



if __name__ == '__main__':
    pins = (5, 6)
    motor = Motor(*pins)

    current_speed = ramp_up(motor, steps)
    time.sleep(2)
    ramp_down(motor, steps)
