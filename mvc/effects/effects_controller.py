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
        self.to_patches_controller(self.actions.to_next_patch())

    def to_before_patch(self):
        self.to_patches_controller(self.actions.to_before_patch())

    ##########################
    # Actions
    ##########################
    def toggle_status_effect(self):
        print(self.current_effect.index, self.current_effect['name'])
        self.actions.toggle_status_effect(self.current_effect)

    def to_next_effect(self):
        index = self.current_effect.index + 1
        if index != len(self.current_patch.effects):
            self.to_effect(index)

    def to_before_effect(self):
        index = self.current_effect.index - 1
        if index != -1:
            self.to_effect(index)

    def to_effect(self, effect_index):
        effect = self.current_patch.effects[effect_index]
        self.actions.current_effect = effect
        self.init(self.current_patch, effect)

    ##########################
    # Set controller
    ##########################
    def to_patches_controller(self, patch):
        from raspberry_p1.mvc.patches.patches_controller import PatchesController
        self.start_controller(PatchesController, patch)

    def to_params_controller(self):
        if self.current_effect is None:
            return

        from mvc.params.ParamsController import ParamsController
        self.start_controller(ParamsController, self.current_effect)
