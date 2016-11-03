# -*- coding: utf-8 -*-
from gpiozero import Button, LED


class EffectComponent(object):

    def __init__(self, pin_button, pin_led, pull_up=False):
        self.button = Button(pin_button, pull_up=pull_up)
        self.led = LED(pin_led)
        self._effect = None

    @property
    def action(self):
        return self.button.when_pressed

    @action.setter
    def action(self, data):
        self.button.when_pressed = lambda: [self._update_led(), data()]

    def _update_led(self):
        if self.effect is not None:
            self.led.toggle()
        else:
            self.led.off()

    @property
    def effect(self):
        return self._effect

    @effect.setter
    def effect(self, effect):
        """
        Update this component status by :param effect
        """
        self._effect = effect
        if effect is not None:
            self.led.value = effect.status
        else:
            self.led.off()

    def active(self):
        self.led.off()

    def disable(self):
        self.led.on()
