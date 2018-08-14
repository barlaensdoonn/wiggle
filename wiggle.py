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

    def __init__(self, forward, backward, pwm=True, pwm_pin=None, speed=1.0, sleep_time=0.05, interval=21, *args, **kwargs):
        '''
        interval = how many steps to take when ramping
        sleep = time to sleep between ramp intervals
        '''
        gpiozero.Motor.__init__(self, forward, backward, pwm=pwm, *args, **kwargs)
        self.pins = {'forward': forward, 'backward': backward}
        self.pwm_pin = self._init_pwm_pin(pwm_pin) if pwm_pin else None
        self.speed = speed
        self.interval = interval
        self.sleep_time = sleep_time
        self.steps = self._get_steps()
        self.current_speed = 0

    def _init_pwm_pin(self, pwm_pin):
        '''set pwm_pin to HIGH. i think it has to be on for reference voltage or something'''
        mypwm = gpiozero.OutputDevice(pwm_pin)
        mypwm.on()
        return mypwm

    def _get_steps(self):
        '''
        numpy.arange results in: array([0. ,  0.1,  0.2,  0.3,  0.4,  0.5,  0.6,  0.7,  0.8,  0.9])
        using numpy.linspace to create steps ensures the last number will always be 1
        '''
        return numpy.linspace(0, self.speed, self.interval)

    def ramp_up(self):
        self.steps = self._get_steps()
        for step in self.steps:
            self.forward(speed=step)
            self.current_speed = step
            time.sleep(self.sleep_time)

    def ramp_down(self):
        '''have to add 1 to because regular indexing starts @ 0, but reverse indexing starts @ -1'''
        self.steps = self._get_steps()
        for step in range(len(self.steps)):
            step += 1
            step *= -1
            speed = self.steps[step]

            self.forward(speed=speed)
            self.current_speed = speed
            time.sleep(self.sleep_time)

    def test(self):
        self.ramp_up()
        time.sleep(2)
        self.ramp_down()


if __name__ == '__main__':
    pins_a = (5, 6)
    pins_b = (13, 19)
    pwm_a = 17
    pwm_b = 18
    wiggler_a = Wiggler(*pins_a, pwm_pin=pwm_a)
    wiggler_b = Wiggler(*pins_b, pwm_pin=pwm_b)

    wiggler_a.test()
    wiggler_b.test()
