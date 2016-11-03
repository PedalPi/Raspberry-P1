# -*- coding: utf-8 -*-
from gpiozero import Button


class PatchComponent(object):
    button = None

    def __init__(self, pin, pull_up=False):
        self.button = Button(pin, pull_up=pull_up)

    @property
    def action(self):
        return self.button.when_pressed

    @action.setter
    def action(self, data):
        self.button.when_pressed = data
