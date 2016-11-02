# -*- coding: utf-8 -*-
from gpiozero import Button, LED


class EffectComponent(object):
    _effect = None

    def __init__(self, pin_button, pin_led, pull_up=False):
        self.button = Button(pin_button, pull_up=pull_up)
        self.led = LED(pin_led)

    @property
    def action(self):
        return self.button.when_pressed

    @action.setter
    def action(self, data):
        print('effect component initialized')
        self.button.when_pressed = lambda: [data(), self.led.toggle()]

    @property
    def effect(self):
        return self._effect

    @effect.setter
    def effect(self, effect):
        """
        Update this component status by :param effect
        """
        self._effect = effect
        if effect.status:
            self.led.on()
        else:
            self.led.off()

    def active(self):
        pass

    def disable(self):
        pass
