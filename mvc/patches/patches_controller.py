from raspberry_p1.mvc.controller import Controller
from raspberry_p1.mvc.patches.patches_view import PatchesView


class PatchesController(Controller):

    def __init__(self, equipment):
        super().__init__(equipment, PatchesView)
        self.current_patch = None
        self.current_effect = None

    def init(self, current_patch):
        self.current_patch = current_patch
        self.current_effect = self.actions.current_effect
        self.view.show_patch(self.current_patch, self.current_effect)

    ##########################
    # Observer
    ##########################
    def on_current_patch_change(self, patch, token=None):
        self.init(patch)

    ##########################
    # Actions
    ##########################
    def to_next_patch(self):
        next_patch = self.actions.to_next_patch()
        self.init(next_patch)

    def to_before_patch(self):
        before_patch = self.actions.to_before_patch()
        self.init(before_patch)

    def toggle_status_effect(self):
        effect = self.current_effect

        if effect is None:
            return

        self.actions.toggle_status_effect(effect)
        self.to_effects_controller()

    ##########################
    # Set controller
    ##########################
    def to_effects_controller(self):
        if self.current_effect is None:
            return

        from raspberry_p1.mvc.effects.effects_controller import EffectsController

        controller = self.controllers[EffectsController]
        controller.start()
        controller.init(self.current_patch, self.current_effect)
