# -*- coding: utf-8 -*-
from physical.mvc.controller import Controller
from raspberry_p1.mvc.patches.patches_view import PatchesView


class PatchesController(Controller):
    index_effect_focused = 0
    current_patch = None

    def __init__(self, controllers, components, actions, observer):
        super().__init__(controllers, components, actions, observer, PatchesView)

    def init(self, current_patch):
        self.current_patch = current_patch
        self.view.show_patch(self.current_patch)

    def on_current_patch_change(self, patch, token=None):
        self.init(patch)

    def to_next_patch(self):
        next_patch = self.actions.to_next_patch()
        self.init(next_patch)

    def to_before_patch(self):
        before_patch = self.actions.to_before_patch()
        self.init(before_patch)

    def toggle_status_effect(self):
        print('Click')
        '''
        effect = self.current_effect
        if effect is None:
            return

        print("Effect:", effect['uri'])
        print(" - Index:", self.index_effect_focused)
        print(" - Old status:", effect.status)
        self.actions.toggle_status_effect(effect)
        print(" - New status:", effect.status)
        '''

    def to_effects_controller(self):
        print('Encoder click')
        '''
        from raspberry_p1.mvc.effects.EffectsController import EffectsController

        controller = self.controllers[EffectsController]
        controller.start()
        controller.init(self.current_patch)
        '''
