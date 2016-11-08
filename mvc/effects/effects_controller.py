from raspberry_p1.mvc.controller import Controller
from raspberry_p1.mvc.effects.effects_view import EffectsView


class EffectsController(Controller):

    def __init__(self, equipment):
        super().__init__(equipment, EffectsView)
        self.current_patch = None
        self.current_effect = None

    def init(self, current_patch, current_effect):
        self.current_patch = current_patch
        self.current_effect = current_effect

        self.view.show_effect(self.current_effect)

    ##########################
    # Observer
    ##########################
    def on_current_patch_change(self, patch, token=None):
        self.init(patch, self.current_effect)

    ##########################
    # Actions - Patch page
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

        print("Effect:", effect['uri'])
        print(" - Index:", self.index_effect_focused)
        print(" - Old status:", effect.status)
        self.actions.toggle_status_effect(effect)
        print(" - New status:", effect.status)

    ##########################
    # Actions
    ##########################
    def to_next_effect(self):
        index = self.current_effect.index + 1
        if index == len(self.current_patch.effects):
            return

        effect = self.current_patch.effects[index]
        self.actions.current_effect = effect
        self.init(self.current_patch, effect)

    def to_before_effect(self):
        index = self.current_effect.index - 1
        if index == -1:
            return

        effect = self.current_patch.effects[index]
        self.actions.current_effect = effect
        self.init(self.current_patch, effect)

    ##########################
    # Set controller
    ##########################
    def to_patches_controller(self):
        if self.current_effect is None:
            return

        from raspberry_p1.mvc.patches.patches_controller import PatchesController

        controller = self.controllers[PatchesController]
        controller.start()
        controller.init(self.current_patch)

    def to_params_controller(self):
        if self.current_effect is None:
            return

        from mvc.params.ParamsController import ParamsController

        controller = self.controllers[ParamsController]
        controller.start()
        controller.init(self.current_effect)
