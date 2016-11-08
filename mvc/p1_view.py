from abc import ABCMeta

from raspberry_p1.mvc.view import View
from raspberry_p1.component.components import Components


class P1View(View, metaclass=ABCMeta):
    controller = None

    display = None
    next_patch = None
    before_patch = None
    effect = None
    rotary_encoder = None

    def init(self, controller):
        self.controller = controller

    def init_components(self, components):
        self.display = components[Components.DISPLAY]

        self.next_patch = components[Components.NEXT_PATCH]
        self.before_patch = components[Components.BEFORE_PATCH]

        self.effect = components[Components.EFFECT]

        self.rotary_encoder = components[Components.ROTARY_ENCODER]
