#!/usr/bin/python3
# gpiozero - control DC motor
# 12/15/17
# updated: 12/24/17

import time
import numpy
import gpiozero


class Wiggler(gpiozero.Motor):
    '''
    class to extend gpiozero.Motor, which has following methods:
    forward(speed=float)
    backward(speed=float)
    stop()

    speed can only be 0 or 1 if pwm!=True when constructing gpiozero.Motor
    more here: https://gpiozero.readthedocs.io/en/stable/api_output.html#motor
    '''

    def __init__(self, pins, pwm=True, sleep_time=0.05, interval=21):
        '''
        numpy.arange results in: array([0. ,  0.1,  0.2,  0.3,  0.4,  0.5,  0.6,  0.7,  0.8,  0.9])
        using numpy.linspace to create steps ensures the last number will always be 1
        '''

        gpiozero.Motor.__init__(self, *pins, pwm=pwm, *args, **kwargs)
        self.sleep_time = sleep_time
        self.interval = interval
        self.steps = numpy.linspace(0, 1, self.interval)
        self.current_speed = 0

    def ramp_up(self):
        for step in self.steps:
            self.forward(speed=step)
            self.current_speed = step
            time.sleep(self.sleep_time)

    def ramp_down(self):
        '''have to add 1 to because regular indexing starts @ 0, but reverse indexing starts @ -1'''

        for step in range(len(self.steps)):
            step += 1
            step *= -1
            self.forward(speed=steps[step])
            self.current_speed = step
            time.sleep(self.sleep_time)


if __name__ == '__main__':
    pins = (5, 6)
    wiggler = Wiggler(*pins)

    wiggler.ramp_up()
    time.sleep(2)
    wiggler.ramp_down()
